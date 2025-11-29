# ADR 0002: Use Self-Signed Certificates for Development

- Status: Accepted
- Date: 2025-11-29

## Context

We need HTTPS for the checksum demo during development, but using a
third-party CA is unnecessary and adds cost and domain ownership overhead.
Java Keytool can generate self-signed certificates locally with no extra
installation beyond the JDK.

## Decision

Use a self-signed certificate generated with Java Keytool for development:

- Generate a 2048-bit RSA key pair with alias `selfsigned`, validity 360 days,
  stored in `keystore.jks`.
- Use `-exportcert` to write `server.cer` and `-printcert` to verify details.
- In examples, quote passwords that contain characters like `!` to avoid shell
  history expansion on macOS/Linux (for example, `'ExamplePass123!'`).
- Keep keystores/certs local (ignored via `.gitignore`); do not commit them.

## Consequences

- Developers can stand up HTTPS locally without external CA dependencies.
- Browsers will warn because the cert is self-signed; acceptable for local use.
- For production, switch to a trusted CA-issued certificate and replace the
  keystore configuration.

## References

- Certificate generation requirements:
  `doc/requirements/certificate-generation/requirements.md`
- README certificate generation section: `README.md`
