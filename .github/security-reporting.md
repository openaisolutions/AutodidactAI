# Security checks and reporting

Repository: openaisolutions/AutodidactAI

## Automated coverage

The Security CodeQL workflow analyzes python, actions on pull requests, pushes to main, weekly, and on manual dispatch. Findings appear under GitHub Security > Code scanning; execution failures appear in Actions. Analysis uses no-build extraction and does not install or execute project code. Actions are pinned to reviewed upstream commit IDs; Dependabot proposes updates.

Dependabot checks github-actions weekly and opens update pull requests. Each update still requires review and applicable tests. A configured check is not evidence of a successful run or remediation.

## Reporting and closure

For each validated issue, record the repository and commit, affected path, severity, attacker prerequisites, impact, redacted evidence, owner, fix pull request, verification result, and closure date. Keep suspected issues separate from validated findings. Link reports to the relevant CodeQL alert, dependency update, or private security advisory. Never put live credentials or private exploitation details in public issues or workflow logs. Rotate exposed credentials through their issuer and remove exposure from current source; deletion alone does not revoke a credential.

Close an issue only after the fix is merged and verification passes. Track scanner failures and unsupported surfaces separately from clean scans. Review the Security and Actions views across all projects as part of the existing reporting process; this file does not claim a separate reporting dashboard has been integrated.

## Remaining host controls

An administrator must verify secret scanning/push protection availability, dependency alerts, required security checks and branch rules, allowed Actions policy, repository visibility, collaborator access, and private vulnerability reporting. These settings are not controlled by this file. Do not mark the repository secure merely because this baseline is installed. Full source audits, credential rotation where required, and application/runtime reviews remain separate work.

## References

- https://docs.github.com/en/code-security/concepts/supply-chain-security/about-the-dependabot-yml-file
- https://docs.github.com/en/code-security/how-tos/find-and-fix-code-vulnerabilities/manage-your-configuration/codeql-for-compiled-languages
