#!/usr/bin/env python3
"""
release.py — Script de publicação automática
Context Guardian — Skill para Claude.ai

Uso:
    python release.py <versão> "<descrição>"
    python release.py 1.1.0 "Novos comandos de ativação em inglês"

O que faz automaticamente:
    1. Monta o .zip com os arquivos que o Claude precisa (context-guardian/SKILL.md + references/)
    2. git add, commit e push
    3. Cria a release no GitHub via API
    4. Faz upload do .zip como anexo da release

──────────────────────────────────────────────────────────────
CONFIGURAÇÃO DO TOKEN (faça uma única vez, nunca edite aqui)
──────────────────────────────────────────────────────────────

O token do GitHub NUNCA deve ser escrito neste arquivo —
ele ficaria visível no git e seria bloqueado pelo GitHub.

Opção A — Arquivo .github_config (recomendado para uso local):

  Crie o arquivo .github_config na mesma pasta do release.py
  com o seguinte conteúdo (sem aspas):

      GITHUB_USER=brunoflma
      GITHUB_REPO=context-guardian
      GITHUB_TOKEN=ghp_xxxxxxxxxxxx

  Este arquivo está no .gitignore — nunca será commitado.

Opção B — Variáveis de ambiente:

  Windows (PowerShell):
      $env:GITHUB_USER  = "brunoflma"
      $env:GITHUB_REPO  = "context-guardian"
      $env:GITHUB_TOKEN = "ghp_xxxxxxxxxxxx"

  Mac/Linux:
      export GITHUB_USER="brunoflma"
      export GITHUB_REPO="context-guardian"
      export GITHUB_TOKEN="ghp_xxxxxxxxxxxx"

Como criar o token:
    1. Acesse https://github.com/settings/tokens
    2. "Generate new token (classic)"
    3. Marque a permissão: repo (acesso completo)
    4. Clique em "Generate token" e salve o valor no .github_config
──────────────────────────────────────────────────────────────
"""

import os
import sys
import json
import zipfile
import subprocess
import urllib.request
import urllib.error
import re


def load_config():
    config = {}
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".github_config")
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    key, _, val = line.partition("=")
                    val = val.strip().strip('"').strip("'")
                    config[key.strip()] = val
    for key in ("GITHUB_USER", "GITHUB_REPO", "GITHUB_TOKEN"):
        if os.environ.get(key):
            config[key] = os.environ[key]
    return config


def validate_config(config):
    missing = [k for k in ("GITHUB_USER", "GITHUB_REPO", "GITHUB_TOKEN") if not config.get(k)]
    if missing:
        print("\n❌ Configuração incompleta. Faltam: " + ", ".join(missing))
        print("\nCrie o arquivo .github_config na pasta do projeto com:")
        print("   GITHUB_USER=brunoflma")
        print("   GITHUB_REPO=context-guardian")
        print("   GITHUB_TOKEN=ghp_xxxxxxxxxxxx")
        sys.exit(1)


def log(msg, icon="→"):
    print(f"\n{icon} {msg}")


def run(cmd, check=True):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"\n❌ Erro ao executar: {cmd}")
        if result.stdout.strip():
            print(result.stdout)
        if result.stderr.strip():
            print(result.stderr)
        sys.exit(1)
    return result


def build_zip(version):
    """
    Monta o .zip com APENAS os arquivos que o Claude precisa para instalar a skill.
    Estrutura dentro do zip espelha o que o Claude espera:

        context-guardian/
        ├── SKILL.md
        └── references/
            ├── transfer-report-template.md
            ├── degradation-signals.md
            └── automation-orchestrator.md

    README, CHANGELOG, release.py e .github_config são ferramentas do repositório
    e não devem ser incluídos no zip de instalação.
    """
    zip_name = f"context-guardian-v{version}.zip"

    # src = caminho no repositório | dest = caminho dentro do zip
    files = [
        ("context-guardian/SKILL.md",                                       "context-guardian/SKILL.md"),
        ("context-guardian/references/transfer-report-template.md",         "context-guardian/references/transfer-report-template.md"),
        ("context-guardian/references/degradation-signals.md",              "context-guardian/references/degradation-signals.md"),
        ("context-guardian/references/automation-orchestrator.md",          "context-guardian/references/automation-orchestrator.md"),
    ]

    ALLOWED_IN_ZIP = {dest for _, dest in files}

    missing = [src for src, _ in files if not os.path.exists(src)]
    if missing:
        print(f"\n❌ Arquivos não encontrados:")
        for f in missing:
            print(f"   {f}")
        sys.exit(1)

    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zf:
        for src, dest in files:
            zf.write(src, dest)
            print(f"   + {dest}")

    # Validação: abortar se houver arquivo fora da allowlist
    with zipfile.ZipFile(zip_name, "r") as zf:
        names = set(zf.namelist())
    unexpected = names - ALLOWED_IN_ZIP
    if unexpected:
        os.remove(zip_name)
        print(f"\n❌ ABORTADO — o zip contém arquivos não autorizados:")
        for f in sorted(unexpected):
            print(f"   {f}")
        sys.exit(1)

    size_kb = os.path.getsize(zip_name) // 1024
    print(f"   → {zip_name} ({size_kb} KB) — validado ✓")
    return zip_name


def git_commit_push(version, description):
    NEVER_COMMIT = [".github_config", "github.txt", "secrets.txt"]
    for f in NEVER_COMMIT:
        result = run(f"git ls-files {f}", check=False)
        if result.stdout.strip():
            print(f"\n❌ ABORTADO — '{f}' está sendo rastreado pelo git e contém credenciais.")
            print(f"   Execute: git rm --cached {f}")
            sys.exit(1)

    # Commitar a pasta da skill e os arquivos do repo (sem release.py e .gitignore)
    run('git add -A "context-guardian"', check=False)
    for f in ["README.md", "CHANGELOG.md"]:
        run(f'git add "{f}"', check=False)

    staged = run("git status --porcelain", check=False)
    if not staged.stdout.strip():
        print("   → Nada a commitar — repositório já está atualizado")
    else:
        run(f'git commit -m "release: v{version} — {description}"')

    run("git push --force-with-lease")


def github_api(method, path, data=None, token=None):
    url = f"https://api.github.com{path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"\n❌ Erro na API do GitHub ({e.code}): {e.read().decode()}")
        sys.exit(1)


def upload_asset(upload_url, zip_path, token):
    base_url = upload_url.split("{")[0]
    filename = os.path.basename(zip_path)
    url = f"{base_url}?name={filename}"
    with open(zip_path, "rb") as f:
        data = f.read()
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/zip",
        "Accept": "application/vnd.github+json",
    }
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"\n❌ Erro ao fazer upload do zip ({e.code}): {e.read().decode()}")
        sys.exit(1)


def get_last_published_version(github_user, github_repo, token):
    try:
        url = f"https://api.github.com/repos/{github_user}/{github_repo}/releases/latest"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
            return data.get("tag_name", "").lstrip("v")
    except Exception:
        return None


def compile_changelog(current_version, last_published_version):
    if not os.path.exists("CHANGELOG.md"):
        return f"Versão {current_version}"
    with open("CHANGELOG.md", "r", encoding="utf-8") as f:
        content = f.read()
    pattern = re.compile(r'^## v([\d.]+)', re.MULTILINE)
    matches = list(pattern.finditer(content))
    if not matches:
        return f"Versão {current_version}"

    def ver_tuple(v):
        try:
            return tuple(int(x) for x in v.split('.'))
        except Exception:
            return (0,)

    current_t = ver_tuple(current_version)
    last_t    = ver_tuple(last_published_version) if last_published_version else (0,)
    entries = []
    for i, m in enumerate(matches):
        v = m.group(1)
        v_t = ver_tuple(v)
        if last_t < v_t <= current_t:
            start = m.start()
            end   = matches[i+1].start() if i+1 < len(matches) else len(content)
            block = content[start:end].strip()
            lines = block.split('\n')[1:]
            entries.append(f"### v{v}\n" + "\n".join(lines).strip())

    if not entries:
        start = content.find(f"## v{current_version}")
        if start == -1:
            return f"Versão {current_version}"
        end = content.find("\n## ", start + 1)
        block = content[start:end].strip() if end != -1 else content[start:].strip()
        lines = block.split("\n")[1:]
        return "\n".join(lines).strip()

    return "\n\n".join(entries)


def main():
    if len(sys.argv) < 3:
        print("Uso: python release.py <versão> \"<descrição>\"")
        print('Ex:  python release.py 1.1.0 "Novos comandos de ativação em inglês"')
        sys.exit(1)

    config = load_config()
    validate_config(config)

    GITHUB_USER  = config["GITHUB_USER"]
    GITHUB_REPO  = config["GITHUB_REPO"]
    GITHUB_TOKEN = config["GITHUB_TOKEN"]

    version     = sys.argv[1].lstrip("v")
    description = sys.argv[2]
    tag         = f"v{version}"

    print(f"\n{'━'*50}")
    print(f"  Publicando Context Guardian v{version}")
    print(f"  {description}")
    print(f"{'━'*50}")

    log("Montando o arquivo .zip...")
    zip_path = build_zip(version)

    log("Commitando e publicando no GitHub...")
    git_commit_push(version, description)
    print("   → Push concluído")

    log("Criando a release no GitHub...")
    last_version = get_last_published_version(GITHUB_USER, GITHUB_REPO, GITHUB_TOKEN)
    if last_version:
        print(f"   → Última versão publicada: v{last_version}")
    notes = compile_changelog(version, last_version)
    intro = f"v{last_version} → v{version}" if last_version else f"v{version}"
    release_body = (
        f"## {intro}\n\n{notes}\n\n---\n\n"
        f"Baixe o arquivo zip abaixo e instale no Claude.ai em **Configurações → Skills → Instalar Skill**."
    )

    release = github_api(
        "POST",
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/releases",
        data={
            "tag_name":   tag,
            "name":       f"Context Guardian v{version} — {description}",
            "body":       release_body,
            "draft":      False,
            "prerelease": False,
        },
        token=GITHUB_TOKEN,
    )
    print(f"   → Release criada: {release['html_url']}")

    log("Fazendo upload do .zip...")
    asset = upload_asset(release["upload_url"], zip_path, GITHUB_TOKEN)
    print(f"   → Download: {asset['browser_download_url']}")

    os.remove(zip_path)
    print(f"   → Zip local removido")

    print(f"\n{'━'*50}")
    print(f"  ✅ v{version} publicada com sucesso!")
    print(f"  🔗 {release['html_url']}")
    print(f"{'━'*50}\n")


if __name__ == "__main__":
    main()
