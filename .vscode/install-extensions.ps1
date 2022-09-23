#requires -PSEdition Core

Get-Content .vscode/extensions.list |% { code.cmd --install-extension $_ }
