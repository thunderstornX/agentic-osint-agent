# Ethical Use Policy

`agentic-osint-agent` is a passive-reconnaissance tool that exercises **public,
read-only data sources only**: WHOIS records, the Shodan InternetDB free
endpoint, the GitHub public search API, the Wayback Machine CDX API, and
public DNS resolvers.

It does not scan ports, deliver payloads, attempt authentication against the
target, or send traffic to anything other than the third-party data sources
listed above.

```
                  .-----.
                 / o   o \             ~ follow the threads, not the targets ~
                |    >    |
                 \  ___  /
                  '--Y--'
                    | |
                    | |
                    | |
                __ -' `- __
              .'           '.
             /   ~~~~~~~~~   \
            |    publicly     |
             \   sourced     /
              '. _________ .'
```

## In scope

- Targets you operate yourself.
- Targets you have **written authorisation** to investigate (red-team
  engagement letter, bug-bounty programme rules, incident-response mandate,
  academic research with IRB approval).
- Public-interest targets where passive reconnaissance is lawful in the
  operator's jurisdiction (`.gov`, `.edu`, large public companies that
  publish responsible-disclosure programmes).

## Out of scope

- Private individuals, especially named natural persons.
- Domains belonging to organisations smaller than ~50 employees, where the
  reidentification risk for private individuals is high.
- Targets in jurisdictions where passive OSINT against the target is itself
  a regulated activity without a licence.
- Any active probing, login attempts, vulnerability triggering, or
  credential testing against the target. This tool **does not** do that, and
  if you bolt that on, it is no longer this tool.

## Operator responsibilities

- Capture the legal basis for the investigation **before** running the
  agent. The structured JSON report has a `operator_authority` field that
  must be filled in (see `output/formatter.py`).
- Treat the resulting report as **sensitive intelligence**. Findings about a
  target's open ports, exposed config files, or historical web pages are
  not abuse on their own, but enable abuse if leaked.
- Respect the rate limits of the third-party data sources. The default
  configuration is well below all of them; do not raise it just because you
  can.

## What "agentic" does NOT mean here

The agent does **not** make decisions about the operator's legal posture,
reidentify private individuals from public data, scrape personal social
media profiles, or contact targets. Its autonomy is limited to *which
public source to query next* — not *whom to investigate*.

## Reporting concerns

If this repository is used in a way that violates this policy, contact
the author at the address in `CITATION.cff`.

## Companion documents

- The agent operates within the framework described in *Operationalising the
  OSINT Lifecycle: A Framework for Privacy-Aware and Compliant OSINT
  Operations* — Zenodo DOI [10.5281/zenodo.16924934](https://doi.org/10.5281/zenodo.16924934).
