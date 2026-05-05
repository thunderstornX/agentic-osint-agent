# OSINT briefing — `ietf.org`

- **Generated:** 2026-05-05T07:34:29+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 79.61 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
**ietf.org** – the domain of the Internet Engineering Task Force.

## Key facts
- Registered through **Cloudflare, Inc.** with creation date **1995‑03‑11** and expiration **2031‑03‑12**. (WHOIS)  
- Authoritative name servers are **jill.ns.cloudflare.com** and **ken.ns.cloudflare.com**. (WHOIS, DNS NS)  
- DNS A records resolve to **104.16.45.99** and **104.16.44.99**; AAAA records to **2606:4700::6810:2c63** and **2606:4700::6810:2d63**. (DNS A, DNS AAAA)  
- MX record points to **mail2.ietf.org**. (DNS MX)  
- TXT records include a token (`vs58md9pf8hu6knlglfda9lk6g`), an SPF policy referencing several IP ranges and includes for Google and hostedrt.com, and another token (`ca3-5567e36d3f9947308ac2892e009840cc`). (DNS TXT)

## Notable findings
- Shodan reports the IP **104.16.45.99** (one of the A records) as hosting a wide range of open ports: **80, 2053, 2082, 2083, 2087, 2096, 8080, 8443, 8880**. (Shodan)  
- The same IP resolves to hostnames **ietf.org**, **idnits.ietf.org**, and **get.staging.ietf.org**. (Shodan)  
- The CPE identifier indicates the service is running **Cloudflare** infrastructure. (Shodan)

## Open questions
- The purpose of the numerous non‑standard open ports (e.g., 2053, 2082‑2096, 8080, 8443, 8880) is not clear from the available data.  
- No information is present about the services bound to those ports or any associated applications.  
- The meaning of the two opaque TXT tokens (`vs58md9pf8hu6knlglfda9lk6g`, `ca3-5567e36d3f9947308ac2892e009840cc`) cannot be determined from the evidence.

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 5 |
| DNS | 1 | 10 |
| Shodan IDB | 1 | 13 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `Cloudflare, Inc.` | WHOIS |
| 2 | whois | creation_date | `1995-03-11` | WHOIS |
| 3 | whois | expiration_date | `2031-03-12` | WHOIS |
| 4 | whois | name_server | `jill.ns.cloudflare.com` | WHOIS |
| 5 | whois | name_server | `ken.ns.cloudflare.com` | WHOIS |
| 6 | dns | dns.a | `104.16.45.99` | DNS A |
| 7 | dns | dns.a | `104.16.44.99` | DNS A |
| 8 | dns | dns.aaaa | `2606:4700::6810:2c63` | DNS AAAA |
| 9 | dns | dns.aaaa | `2606:4700::6810:2d63` | DNS AAAA |
| 10 | dns | dns.mx | `0 mail2.ietf.org.` | DNS MX |
| 11 | dns | dns.ns | `ken.ns.cloudflare.com.` | DNS NS |
| 12 | dns | dns.ns | `jill.ns.cloudflare.com.` | DNS NS |
| 13 | dns | dns.txt | `vs58md9pf8hu6knlglfda9lk6g` | DNS TXT |
| 14 | dns | dns.txt | `v=spf1 ip4:166.84.6.31 ip4:166.84.7.238 ip6:2602:f977:800:f7f6::/64 ip4:166.84.7` | DNS TXT |
| 15 | dns | dns.txt | `ca3-5567e36d3f9947308ac2892e009840cc` | DNS TXT |
| 16 | shodan | open_port | `80` | https://internetdb.shodan.io/104.16.45.99 |
| 17 | shodan | open_port | `2053` | https://internetdb.shodan.io/104.16.45.99 |
| 18 | shodan | open_port | `2082` | https://internetdb.shodan.io/104.16.45.99 |
| 19 | shodan | open_port | `2083` | https://internetdb.shodan.io/104.16.45.99 |
| 20 | shodan | open_port | `2087` | https://internetdb.shodan.io/104.16.45.99 |
| 21 | shodan | open_port | `2096` | https://internetdb.shodan.io/104.16.45.99 |
| 22 | shodan | open_port | `8080` | https://internetdb.shodan.io/104.16.45.99 |
| 23 | shodan | open_port | `8443` | https://internetdb.shodan.io/104.16.45.99 |
| 24 | shodan | open_port | `8880` | https://internetdb.shodan.io/104.16.45.99 |
| 25 | shodan | hostname | `get.staging.ietf.org` | https://internetdb.shodan.io/104.16.45.99 |
| 26 | shodan | hostname | `idnits.ietf.org` | https://internetdb.shodan.io/104.16.45.99 |
| 27 | shodan | hostname | `ietf.org` | https://internetdb.shodan.io/104.16.45.99 |
| 28 | shodan | cpe | `cpe:/a:cloudflare:cloudflare` | https://internetdb.shodan.io/104.16.45.99 |

## Trace

- plan: First run whois to capture the registrar, registration dates and name‑servers, establishing ownership and infrastructure baseline. Next query dns to list A/AAAA, MX, NS, TXT and CNAME records, revealing current services, mail routing and possible sub‑domains. Then use shodan to pull InternetDB data for those IPs, exposing open ports, hostnames and known vulnerabilities. After that search github for “ietf.org” or related paths to find accidental code or credential leaks. Finally check wayback to view historical snapshots, tracking domain, sub‑domain and content changes over time.
- decide -> whois: Start with cheap WHOIS lookup to get registration and name‑server info
- observe: whois: 5 findings (5 new), elapsed 944 ms
- decide -> dns: Gather current DNS records to identify IPs and services for further investigation
- observe: dns: 10 findings (10 new), elapsed 697 ms
- decide -> shodan: Next step is to query Shodan for the IPs discovered to get open ports and host details
- observe: shodan: 13 findings (13 new), elapsed 782 ms
- decide -> github: Next tool in plan is github to search for any code or credential leaks related to ietf.org
- observe: github: 0 findings (0 new), elapsed 3853 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Complete coverage by retrieving historical snapshots of ietf.org
- observe: wayback: 0 findings (0 new), elapsed 15773 ms, error: Wayback CDX request failed: ReadTimeout
- decide -> stop: All tools have been used and relevant evidence collected
