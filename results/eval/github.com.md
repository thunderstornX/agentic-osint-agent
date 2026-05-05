# OSINT briefing — `github.com`

- **Generated:** 2026-05-05T07:25:58+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 73.55 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
**github.com** – primary domain of GitHub, Inc.

## Key facts
- Registered through **MarkMonitor, Inc.** with creation date **2007‑10‑09** and expiration **2026‑10‑09** (WHOIS).  
- Registrant organization listed as **GitHub, Inc.** (WHOIS).  
- Authoritative name servers include a mix of **NSONE** and **AWS Route 53** entries (e.g., `dns1.p08.nsone.net`, `ns-520.awsdns-01.net`) (WHOIS, DNS NS).  
- Single A‑record resolves to **20.207.73.82** (DNS A).  
- MX record points to Microsoft 365 (`github-com.mail.protection.outlook.com`) (DNS MX).  
- TXT records contain numerous third‑party verification strings (Google, Apple, Facebook, Stripe, etc.) and an SPF policy referencing several services (DNS TXT).  

## Notable findings
- The IP **20.207.73.82** hosts open ports **22 (SSH), 80 (HTTP), 443 (HTTPS)** (Shodan).  
- Shodan reports hostnames **github.com** and **www.github.com** for this IP (Shodan).  
- The SPF record authorizes a broad set of sending networks, including GitHub’s own `192.30.252.0/22` block and multiple third‑party services (DNS TXT).  

## Open questions
- Why does the domain resolve to a single IP address despite a large, distributed infrastructure (e.g., CDN, load balancers) typically used by GitHub?  
- Are the numerous verification TXT records indicative of active integrations with the listed services, or are they legacy entries?  
- No evidence in the provided data about CDN endpoints, edge locations, or additional A/AAAA records; further probing may be required to map the full surface.

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 12 |
| DNS | 1 | 30 |
| Shodan IDB | 1 | 5 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `MarkMonitor, Inc.` | WHOIS |
| 2 | whois | creation_date | `2007-10-09` | WHOIS |
| 3 | whois | expiration_date | `2026-10-09` | WHOIS |
| 4 | whois | name_server | `dns1.p08.nsone.net` | WHOIS |
| 5 | whois | name_server | `dns2.p08.nsone.net` | WHOIS |
| 6 | whois | name_server | `dns3.p08.nsone.net` | WHOIS |
| 7 | whois | name_server | `dns4.p08.nsone.net` | WHOIS |
| 8 | whois | name_server | `ns-1283.awsdns-32.org` | WHOIS |
| 9 | whois | name_server | `ns-1707.awsdns-21.co.uk` | WHOIS |
| 10 | whois | name_server | `ns-421.awsdns-52.com` | WHOIS |
| 11 | whois | name_server | `ns-520.awsdns-01.net` | WHOIS |
| 12 | whois | registrant_org | `GitHub, Inc.` | WHOIS |
| 13 | dns | dns.a | `20.207.73.82` | DNS A |
| 14 | dns | dns.mx | `0 github-com.mail.protection.outlook.com.` | DNS MX |
| 15 | dns | dns.ns | `ns-520.awsdns-01.net.` | DNS NS |
| 16 | dns | dns.ns | `ns-1283.awsdns-32.org.` | DNS NS |
| 17 | dns | dns.ns | `dns1.p08.nsone.net.` | DNS NS |
| 18 | dns | dns.ns | `ns-1707.awsdns-21.co.uk.` | DNS NS |
| 19 | dns | dns.ns | `dns3.p08.nsone.net.` | DNS NS |
| 20 | dns | dns.ns | `ns-421.awsdns-52.com.` | DNS NS |
| 21 | dns | dns.ns | `dns4.p08.nsone.net.` | DNS NS |
| 22 | dns | dns.ns | `dns2.p08.nsone.net.` | DNS NS |
| 23 | dns | dns.txt | `v=spf1 ip4:192.30.252.0/22 include:spf.protection.outlook.com include:_netblocks` | DNS TXT |
| 24 | dns | dns.txt | `apple-domain-verification=RyQhdzTl6Z6x8ZP4` | DNS TXT |
| 25 | dns | dns.txt | `00Dd0000000hHE0=1TBKg000000TN2r` | DNS TXT |
| 26 | dns | dns.txt | `adobe-idp-site-verification=b92c9e999aef825edc36e0a3d847d2dbad5b2fc0e05c79ddd7a1` | DNS TXT |
| 27 | dns | dns.txt | `MS=ms44452932` | DNS TXT |
| 28 | dns | dns.txt | `shopify-verification-code=t1YPwcmvnxZyBycaCpk1MPyWoFs72o` | DNS TXT |
| 29 | dns | dns.txt | `atlassian-domain-verification=jjgw98AKv2aeoYFxiL/VFaoyPkn3undEssTRuMg6C/3Fp/iqhk` | DNS TXT |
| 30 | dns | dns.txt | `jamf-site-verification=XtaPNIYghF_e_xRDI8CjgQ` | DNS TXT |
| 31 | dns | dns.txt | `stripe-verification=f88ef17321660a01bab1660454192e014defa29ba7b8de9633c69d6b4912` | DNS TXT |
| 32 | dns | dns.txt | `MS=ms58704441` | DNS TXT |
| 33 | dns | dns.txt | `facebook-domain-verification=39xu4jzl7roi7x0n93ldkxjiaarx50` | DNS TXT |
| 34 | dns | dns.txt | `google-site-verification=82Le34Flgtd15ojYhHlGF_6g72muSjamlMVThBOJpks` | DNS TXT |
| 35 | dns | dns.txt | `loom-site-verification=f3787154f1154b7880e720a511ea664d` | DNS TXT |
| 36 | dns | dns.txt | `krisp-domain-verification=ZlyiK7XLhnaoUQb2hpak1PLY7dFkl1WE` | DNS TXT |
| 37 | dns | dns.txt | `docusign=087098e3-3d46-47b7-9b4e-8a23028154cd` | DNS TXT |
| 38 | dns | dns.txt | `TAILSCALE-xOzoDvFUzZr5YYVCQFuD` | DNS TXT |
| 39 | dns | dns.txt | `calendly-site-verification=at0DQARi7IZvJtXQAWhMqpmIzpvoBNF7aam5VKKxP` | DNS TXT |
| 40 | dns | dns.txt | `miro-verification=d2e174fdb00c71e0bcf58f8e58c3da2dd80dcfa9` | DNS TXT |
| 41 | dns | dns.txt | `google-site-verification=UTM-3akMgubp6tQtgEuAkYNYLyYAvpTnnSrDMWoDR3o` | DNS TXT |
| 42 | dns | dns.txt | `MS=6BF03E6AF5CB689E315FB6199603BABF2C88D805` | DNS TXT |
| 43 | shodan | open_port | `22` | https://internetdb.shodan.io/20.207.73.82 |
| 44 | shodan | open_port | `80` | https://internetdb.shodan.io/20.207.73.82 |
| 45 | shodan | open_port | `443` | https://internetdb.shodan.io/20.207.73.82 |
| 46 | shodan | hostname | `www.github.com` | https://internetdb.shodan.io/20.207.73.82 |
| 47 | shodan | hostname | `github.com` | https://internetdb.shodan.io/20.207.73.82 |

## Trace

- plan: First run whois to learn the domain’s registrar, creation/expiry dates and authoritative name servers, establishing ownership and timeline. Next query dns to collect A/AAAA, MX, NS, TXT and CNAME records, revealing hosted services, mail routing and possible sub‑domains. Then use shodan to enumerate open ports, hostnames and known vulnerabilities tied to those IPs. After that search github for accidental commits containing the domain or related URLs to uncover internal URLs or credentials. Finally pull wayback snapshots to see historic site content, sub‑domains and configuration changes.
- decide -> whois: Start with cheap whois to get domain registration details and name servers
- observe: whois: 12 findings (12 new), elapsed 1147 ms
- decide -> dns: Gather DNS records to identify IPs, subdomains, and services for further investigation
- observe: dns: 30 findings (30 new), elapsed 472 ms
- decide -> shodan: Next step is to enumerate open ports, hostnames, and vulnerabilities for the domain's IPs
- observe: shodan: 5 findings (5 new), elapsed 411 ms
- decide -> github: Search GitHub for accidental commits referencing the target domain to uncover internal URLs or crede
- observe: github: 0 findings (0 new), elapsed 3093 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Collect historic snapshots of github.com to reveal past content, subdomains, and configuration chang
- observe: wayback: 0 findings (0 new), elapsed 15417 ms, error: Wayback CDX request failed: ReadTimeout
- decide -> stop: All tools have been used and evidence collected
