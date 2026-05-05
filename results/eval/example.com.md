# OSINT briefing — `example.com`

- **Generated:** 2026-05-05T07:37:11+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 90.94 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
**example.com** – domain registered with IANA (reserved) and hosted on Cloudflare nameservers.

## Key facts
- Registrar: RESERVED‑Internet Assigned Numbers Authority (WHOIS)  
- Creation date: 14 Aug 1995; expiration: 13 Aug 2026 (WHOIS)  
- Authoritative name servers: `elliott.ns.cloudflare.com` and `hera.ns.cloudflare.com` (WHOIS, DNS NS)  
- DNS A records: `172.66.147.243`, `104.20.23.154` (DNS A)  
- DNS AAAA records: `2606:4700:10::6814:179a`, `2606:4700:10::ac42:93f3` (DNS AAAA)  
- No MX records configured (`0 .`) (DNS MX)  
- TXT records: `v=spf1 -all` and a random string `_k2n1y4vw3qtb4skdx9e7dxt97qrmmq9` (DNS TXT)  

## Notable findings
- The IP `172.66.147.243` (one of the A records) shows many open ports on Shodan: 80, 443, 2052, 2053, 2082, 2083, 2086, 2087, 8080, 8443, 8880 (Shodan).  
- Shodan identifies the host as running Cloudflare software (`cpe:/a:cloudflare:cloudflare`) (Shodan).  
- Presence of non‑standard ports (e.g., 2052‑2087, 8080, 8443, 8880) may indicate additional services or proxy panels behind Cloudflare, but no further detail is available in the evidence.

## Open questions
- What services are bound to the non‑standard open ports (2052‑2087, 8080, 8443, 8880)?  
- Is the second A record (`104.20.23.154`) similarly exposed, and does it host the same set of ports?  
- What is the purpose of the opaque TXT string (`_k2n1y4vw3qtb4skdx9e7dxt97qrmmq9`)?  
- Are there any hidden subdomains or content archived in Wayback or GitHub that were not captured in the provided data?

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 5 |
| DNS | 1 | 9 |
| Shodan IDB | 1 | 12 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `RESERVED-Internet Assigned Numbers Authority` | WHOIS |
| 2 | whois | creation_date | `1995-08-14` | WHOIS |
| 3 | whois | expiration_date | `2026-08-13` | WHOIS |
| 4 | whois | name_server | `elliott.ns.cloudflare.com` | WHOIS |
| 5 | whois | name_server | `hera.ns.cloudflare.com` | WHOIS |
| 6 | dns | dns.a | `172.66.147.243` | DNS A |
| 7 | dns | dns.a | `104.20.23.154` | DNS A |
| 8 | dns | dns.aaaa | `2606:4700:10::6814:179a` | DNS AAAA |
| 9 | dns | dns.aaaa | `2606:4700:10::ac42:93f3` | DNS AAAA |
| 10 | dns | dns.mx | `0 .` | DNS MX |
| 11 | dns | dns.ns | `elliott.ns.cloudflare.com.` | DNS NS |
| 12 | dns | dns.ns | `hera.ns.cloudflare.com.` | DNS NS |
| 13 | dns | dns.txt | `v=spf1 -all` | DNS TXT |
| 14 | dns | dns.txt | `_k2n1y4vw3qtb4skdx9e7dxt97qrmmq9` | DNS TXT |
| 15 | shodan | open_port | `80` | https://internetdb.shodan.io/172.66.147.243 |
| 16 | shodan | open_port | `443` | https://internetdb.shodan.io/172.66.147.243 |
| 17 | shodan | open_port | `2052` | https://internetdb.shodan.io/172.66.147.243 |
| 18 | shodan | open_port | `2053` | https://internetdb.shodan.io/172.66.147.243 |
| 19 | shodan | open_port | `2082` | https://internetdb.shodan.io/172.66.147.243 |
| 20 | shodan | open_port | `2083` | https://internetdb.shodan.io/172.66.147.243 |
| 21 | shodan | open_port | `2086` | https://internetdb.shodan.io/172.66.147.243 |
| 22 | shodan | open_port | `2087` | https://internetdb.shodan.io/172.66.147.243 |
| 23 | shodan | open_port | `8080` | https://internetdb.shodan.io/172.66.147.243 |
| 24 | shodan | open_port | `8443` | https://internetdb.shodan.io/172.66.147.243 |
| 25 | shodan | open_port | `8880` | https://internetdb.shodan.io/172.66.147.243 |
| 26 | shodan | cpe | `cpe:/a:cloudflare:cloudflare` | https://internetdb.shodan.io/172.66.147.243 |

## Trace

- plan: First run whois to capture registrar details, creation/expiry dates and name‑servers, establishing ownership and timeline. Next query dns to list A/AAAA, MX, NS, TXT and CNAME records, revealing current infrastructure, mail routing and possible subdomains. Then use shodan to pull InternetDB data for those IPs, exposing open ports, services, hostnames and known vulnerabilities. After that search github for “example.com” in code, commits and config files to find accidental disclosures. Finally check wayback to view historical snapshots of the site, tracking changes in content, subdomains and technology over time.
- decide -> whois: Start with cheap whois to get registrar and domain registration details
- observe: whois: 5 findings (5 new), elapsed 1011 ms
- decide -> dns: Gather DNS records to map the domain's infrastructure and subdomains
- observe: dns: 9 findings (9 new), elapsed 215 ms
- decide -> shodan: Query Shodan for the discovered IPs to uncover open ports, services, and potential vulnerabilities
- observe: shodan: 12 findings (12 new), elapsed 925 ms
- decide -> github: Next tool in plan is GitHub to search for code disclosures related to example.com
- observe: github: 0 findings (0 new), elapsed 540 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Cover the remaining tool to gather historical site snapshots
- observe: wayback: 0 findings (0 new), elapsed 15828 ms, error: Wayback CDX request failed: ReadTimeout
- decide -> stop: All tools have been used and evidence gathered
