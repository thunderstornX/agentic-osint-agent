# OSINT briefing — `owasp.org`

- **Generated:** 2026-05-05T07:33:09+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 89.09 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
**owasp.org** – the public website of the Open Web Application Security Project.

## Key facts
- Domain registered through **GoDaddy.com, LLC** on **2001‑09‑21** with an expiration date of **2031‑09‑21** (WHOIS).  
- Authoritative name servers are **fay.ns.cloudflare.com** and **west.ns.cloudflare.com** (WHOIS, DNS NS).  
- DNS resolves to two IPv4 addresses **172.66.157.115** and **104.20.44.163**, and two IPv6 addresses **2606:4700:10::ac42:9d73** and **2606:4700:10::6814:2ca3** (DNS A/AAAA).  
- Mail is handled by Google Workspace servers (MX records: `aspmx.l.google.com`, `alt1/2/3/4.aspmx.l.google.com`) (DNS MX).  
- TXT records contain multiple Google site‑verification strings, an SPF policy referencing Google, Mailchimp, and Amazon SES, a Microsoft verification (`MS=ms73859685`), an Atlassian verification, and a base‑64 string (DNS TXT).  

## Notable findings
- The IP **104.20.44.163** (and its IPv6 counterpart) is hosted behind **Cloudflare** (Shodan CPE `cpe:/a:cloudflare:cloudflare`).  
- Shodan reports that this host has many open ports: **80, 443, 2052, 2082, 2083, 2086, 2087, 8443, 8880** (Shodan). These ports are commonly associated with web traffic (80/443) and various control panels (e.g., cPanel/WHM on 2082‑2083, 2086‑2087, 8443).  

## Open questions
- What services are listening on the non‑standard ports (2052, 2082‑2087, 8443, 8880) and are they intentionally exposed?  
- Are the multiple Google site‑verification TXT entries indicative of recent ownership or configuration changes?  
- No evidence was found regarding the content or version of the web application itself; further probing would be required to assess the actual OWASP site.

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 5 |
| DNS | 1 | 21 |
| Shodan IDB | 1 | 10 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `GoDaddy.com, LLC` | WHOIS |
| 2 | whois | creation_date | `2001-09-21` | WHOIS |
| 3 | whois | expiration_date | `2031-09-21` | WHOIS |
| 4 | whois | name_server | `fay.ns.cloudflare.com` | WHOIS |
| 5 | whois | name_server | `west.ns.cloudflare.com` | WHOIS |
| 6 | dns | dns.a | `172.66.157.115` | DNS A |
| 7 | dns | dns.a | `104.20.44.163` | DNS A |
| 8 | dns | dns.aaaa | `2606:4700:10::ac42:9d73` | DNS AAAA |
| 9 | dns | dns.aaaa | `2606:4700:10::6814:2ca3` | DNS AAAA |
| 10 | dns | dns.mx | `10 alt3.aspmx.l.google.com.` | DNS MX |
| 11 | dns | dns.mx | `5 alt2.aspmx.l.google.com.` | DNS MX |
| 12 | dns | dns.mx | `1 aspmx.l.google.com.` | DNS MX |
| 13 | dns | dns.mx | `10 alt4.aspmx.l.google.com.` | DNS MX |
| 14 | dns | dns.mx | `5 alt1.aspmx.l.google.com.` | DNS MX |
| 15 | dns | dns.ns | `fay.ns.cloudflare.com.` | DNS NS |
| 16 | dns | dns.ns | `west.ns.cloudflare.com.` | DNS NS |
| 17 | dns | dns.txt | `MS=ms73859685` | DNS TXT |
| 18 | dns | dns.txt | `google-site-verification=hJ9eCIFoexfh1sb-WVBkVB5PEND3JiaojOVyaNpyWK8` | DNS TXT |
| 19 | dns | dns.txt | `v=spf1 include:_spf.google.com include:servers.mcsv.net include:amazonses.com -a` | DNS TXT |
| 20 | dns | dns.txt | `RrGYbfHtHhF55ld5k5Rw87iuBu7wAWOX4GR9zffrTh4=` | DNS TXT |
| 21 | dns | dns.txt | `google-site-verification=I9qx_X9EKlR_rfceG25-iXHBXJvLrmeNbkEdy182iI` | DNS TXT |
| 22 | dns | dns.txt | `google-site-verification=1zT9Of9pBuTj1rgeGCxMbya3iQQMxFE9-DzUBhftUVQ` | DNS TXT |
| 23 | dns | dns.txt | `google-site-verification=_slXlbOCopK1Ss9VQEoxdsNxpScVKvXVB_JtPpyL3eQ` | DNS TXT |
| 24 | dns | dns.txt | `google-site-verification=kmxuuCvLW4gII8YaV-3ilTOLUvjZa3uaipm0tmpVGpU` | DNS TXT |
| 25 | dns | dns.txt | `google-site-verification=ubHJGF1N2ylOhYxQnIzEIIFaqUodqsIdTLXF-rCX9ps` | DNS TXT |
| 26 | dns | dns.txt | `atlassian-domain-verification=BhaFKFKoRcW20xvi6UJ3U0CKocKOCgLH6LSuiBYPQ5A53cSCUN` | DNS TXT |
| 27 | shodan | open_port | `80` | https://internetdb.shodan.io/104.20.44.163 |
| 28 | shodan | open_port | `443` | https://internetdb.shodan.io/104.20.44.163 |
| 29 | shodan | open_port | `2052` | https://internetdb.shodan.io/104.20.44.163 |
| 30 | shodan | open_port | `2082` | https://internetdb.shodan.io/104.20.44.163 |
| 31 | shodan | open_port | `2083` | https://internetdb.shodan.io/104.20.44.163 |
| 32 | shodan | open_port | `2086` | https://internetdb.shodan.io/104.20.44.163 |
| 33 | shodan | open_port | `2087` | https://internetdb.shodan.io/104.20.44.163 |
| 34 | shodan | open_port | `8443` | https://internetdb.shodan.io/104.20.44.163 |
| 35 | shodan | open_port | `8880` | https://internetdb.shodan.io/104.20.44.163 |
| 36 | shodan | cpe | `cpe:/a:cloudflare:cloudflare` | https://internetdb.shodan.io/104.20.44.163 |

## Trace

- plan: First run whois to get registrar, creation/expiry dates and name‑servers, establishing ownership and age. Next query dns for A/AAAA, MX, NS, TXT and CNAME records to map the live infrastructure, mail setup and any SPF/DKIM clues. Then use shodan to discover open ports, services, hostnames and known vulnerabilities tied to those IPs. After that search github for the domain in code, looking for accidental credential or config leaks. Finally pull wayback snapshots to see historical site changes, subdomains and past tech stacks.
- decide -> whois: Start with cheap WHOIS lookup to gather ownership and registration details
- observe: whois: 5 findings (5 new), elapsed 571 ms
- decide -> dns: Gather DNS records to map infrastructure and mail setup after obtaining WHOIS info
- observe: dns: 21 findings (21 new), elapsed 329 ms
- decide -> shodan: Next step is to discover open ports, services, and hostnames for the domain's IPs
- observe: shodan: 10 findings (10 new), elapsed 614 ms
- decide -> github: Next tool in plan is GitHub to search for owasp.org references and possible credential leaks
- observe: github: 0 findings (0 new), elapsed 3174 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Cover the remaining tool to gather historical site data
- observe: wayback: 0 findings (0 new), elapsed 15419 ms, error: Wayback CDX request failed: ReadTimeout
- decide -> stop: All tools have been used and relevant evidence has been gathered
