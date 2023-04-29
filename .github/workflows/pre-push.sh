#!/bin/sh

allowed_branches="^feature-[0-9]+$"

while read local_ref local_sha remote_ref remote_sha
do
  if ! echo $local_ref | grep -q -E $allowed_branches; then
    echo "ERRO: Não é possível empurrar a branch '$local_ref'. O nome da branch não segue o padrão permitido (feature-[0-9]+)."
    exit 1
  fi
done

exit 0
