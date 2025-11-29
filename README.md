# Checksum Verification Service

Spring Boot sample that generates a checksum for a unique string using a secure
message digest algorithm.

## Docs

- Requirements and rubric:
  [doc/requirements/requirements.md](doc/requirements/requirements.md)
- Submission template:
  [doc/templates/ChecksumVerificationTemplate.md](doc/templates/ChecksumVerificationTemplate.md)
- Protecting sensitive data reading:
  [doc/readings/ProtectingSensitiveData.md](doc/readings/ProtectingSensitiveData.md)
- Changelog: [doc/CHANGELOG.md](doc/CHANGELOG.md)
- Architecture decision records:
  [doc/adrs/index.md](doc/adrs/index.md)
- Quick links index: [index.md](index.md)

## Run locally

- `./mvnw spring-boot:run`
- Open `https://localhost:8443/hash` (accept the self-signed cert). You should
  see your data string, the cipher algorithm name, and the checksum value.
- If port 8443 is already in use, stop the process (for example,
  `lsof -i :8443` then `kill <pid>`) or override the port with
  `./mvnw spring-boot:run -Dspring-boot.run.arguments="--server.port=8444"`.
- Or auto-launch with: `python3 scripts/autolaunch.py` (starts the server,
  waits for port 8443, then opens the `/hash` page).
