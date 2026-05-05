# OSINT briefing — `nasa.gov`

- **Generated:** 2026-05-05T07:00:24+00:00
- **Provider / model:** `nvidia` / `meta/llama-3.3-70b-instruct`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 90.52 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
The target of this investigation is the domain nasa.gov.

## Key facts
The domain nasa.gov was created on 1997-10-02 (WHOIS) and is set to expire on 2026-07-31 (WHOIS). The registrar is get.gov (WHOIS). The domain has multiple name servers, including a1-32.akam.net, a12-64.akam.net, a14-67.akam.net, a5-66.akam.net, a8-66.akam.net, and a9-64.akam.net (WHOIS and DNS NS).

## Notable findings
The domain has a significant number of DNS TXT records, including verification records for Google, Amazon, Atlassian, and OpenAI (DNS TXT). The domain also has open ports 80 and 443, with a hostname of nasa.gov and www.nasa.gov (Shodan IDB). The web server is identified as nginx (Shodan IDB).

## Open questions
The evidence provided is largely related to DNS and WHOIS records, with some information from Shodan. However, the investigation is limited by the lack of data from other tools, such as GitHub and Wayback. Further analysis of these tools may provide additional insights into the target domain. Additionally, the registrant organization is redacted for privacy (WHOIS), which may limit further investigation.

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 10 |
| DNS | 1 | 29 |
| Shodan IDB | 1 | 5 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `get.gov` | WHOIS |
| 2 | whois | creation_date | `1997-10-02` | WHOIS |
| 3 | whois | expiration_date | `2026-07-31` | WHOIS |
| 4 | whois | name_server | `a1-32.akam.net` | WHOIS |
| 5 | whois | name_server | `a12-64.akam.net` | WHOIS |
| 6 | whois | name_server | `a14-67.akam.net` | WHOIS |
| 7 | whois | name_server | `a5-66.akam.net` | WHOIS |
| 8 | whois | name_server | `a8-66.akam.net` | WHOIS |
| 9 | whois | name_server | `a9-64.akam.net` | WHOIS |
| 10 | whois | registrant_org | `REDACTED FOR PRIVACY` | WHOIS |
| 11 | dns | dns.a | `192.0.66.108` | DNS A |
| 12 | dns | dns.aaaa | `2a04:fa87:fffd::c000:426c` | DNS AAAA |
| 13 | dns | dns.mx | `0 nasa-gov.mail.protection.outlook.com.` | DNS MX |
| 14 | dns | dns.ns | `a8-66.akam.net.` | DNS NS |
| 15 | dns | dns.ns | `a1-32.akam.net.` | DNS NS |
| 16 | dns | dns.ns | `a12-64.akam.net.` | DNS NS |
| 17 | dns | dns.ns | `a14-67.akam.net.` | DNS NS |
| 18 | dns | dns.ns | `a5-66.akam.net.` | DNS NS |
| 19 | dns | dns.ns | `a9-64.akam.net.` | DNS NS |
| 20 | dns | dns.txt | `HRlHXyx8jXo+9pIaJWFVBPOLVfeI2biAj3VT1woaTFpp05D5/q6AoD5KpUgws539/d2jl8wBJiEr58OE` | DNS TXT |
| 21 | dns | dns.txt | `MS=ms93625004` | DNS TXT |
| 22 | dns | dns.txt | `uechcfoubh169akghg2214p54n` | DNS TXT |
| 23 | dns | dns.txt | `atlassian-domain-verification=oNzRM7G9GIAL/LLP5c7sPOQiAHsHrQ1hKcU7GGZ0ADRZJFhUB/` | DNS TXT |
| 24 | dns | dns.txt | `openai-domain-verification=dv-CO0ENDLO7EB9V5E4JnmE6pS8` | DNS TXT |
| 25 | dns | dns.txt | `nmh1f9tgxhmfmjkshg7qh595drdfgnf1` | DNS TXT |
| 26 | dns | dns.txt | `amazonses:PvUL7T41LO87xjr+2nfgxTu11i75NeT9HzY3xYv82Ko=` | DNS TXT |
| 27 | dns | dns.txt | `google-site-verification=ZKpcXLqaBX3jND8Fybkvr3MaaOpC_6MRjXBYm0XNkJQ` | DNS TXT |
| 28 | dns | dns.txt | `pvv8mevb6qrmqvqi8alhmreg42` | DNS TXT |
| 29 | dns | dns.txt | `mj8729pr7k44dx62wwtx5745xr5njzkn` | DNS TXT |
| 30 | dns | dns.txt | `google-site-verification=BUxd0xTJY4ZjGohBwKDpNms-yOATz92Y54kgme4eKHs` | DNS TXT |
| 31 | dns | dns.txt | `v=spf1 include:_spf-4a.nasa.gov include:_spf-4b.nasa.gov include:_spf-4c.nasa.go` | DNS TXT |
| 32 | dns | dns.txt | `1HqDXPHdt8JOt02qy6FB+l3+Z1zXScqcPxlE/faXjZLS9FRbVhHCUCHQE2bWofZt2TWKPchjjma3Pqli` | DNS TXT |
| 33 | dns | dns.txt | `amazonses:FXFVeQnEO3Wua+aY/H4aOIH3sSwteE+7YpGrwm8kF/s=` | DNS TXT |
| 34 | dns | dns.txt | `atlassian-sending-domain-verification=4730ddf4-d24e-4a91-9612-cb14998d0e47` | DNS TXT |
| 35 | dns | dns.txt | `apple-domain-verification=qw51K0kGzRHLbN9S` | DNS TXT |
| 36 | dns | dns.txt | `n39n7frbwnkhcmky2nps779y4ttn61wl` | DNS TXT |
| 37 | dns | dns.txt | `webexdomainverification.1YPST=f98a61ea-b92e-41f2-87aa-5651b2af43b8` | DNS TXT |
| 38 | dns | dns.txt | `openai-domain-verification=dv-Fbq5PVntP9qLelQPUBKniDjr` | DNS TXT |
| 39 | dns | dns.txt | `docusign=4025560e-93c9-4920-bb13-849c6fc35d58` | DNS TXT |
| 40 | shodan | open_port | `80` | https://internetdb.shodan.io/192.0.66.108 |
| 41 | shodan | open_port | `443` | https://internetdb.shodan.io/192.0.66.108 |
| 42 | shodan | hostname | `nasa.gov` | https://internetdb.shodan.io/192.0.66.108 |
| 43 | shodan | hostname | `www.nasa.gov` | https://internetdb.shodan.io/192.0.66.108 |
| 44 | shodan | cpe | `cpe:/a:f5:nginx` | https://internetdb.shodan.io/192.0.66.108 |

## Trace

- plan: I will start with whois for registrar and domain info, then dns for network configuration, followed by shodan for open ports and vulnerabilities, github for potential code leaks, and finally wayback for historical snapshots and changes.
- decide -> whois: Starting with whois to gather registrar and domain information as per the initial plan.
- observe: whois: 10 findings (10 new), elapsed 1167 ms
- decide -> dns: Next cheap tool to gather network configuration information.
- observe: dns: 29 findings (29 new), elapsed 1386 ms
- decide -> shodan: Next expensive tool to explore open ports and vulnerabilities after gathering registrar and network 
- observe: shodan: 5 findings (5 new), elapsed 483 ms
- decide -> github: To search for potential code leaks related to nasa.gov
- observe: github: 0 findings (0 new), elapsed 3005 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: The only remaining tool to be called is wayback to gather historical snapshots and changes.
- observe: wayback: 0 findings (0 new), elapsed 15314 ms, error: Wayback CDX request failed: ReadTimeout
- decide -> stop: All five tools have been called at least once and there are findings.
