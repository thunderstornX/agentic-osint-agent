# OSINT briefing — `iana.org`

- **Generated:** 2026-05-05T07:35:40+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 71.3 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
**iana.org** – the Internet Assigned Numbers Authority website.

## Key facts
- Registered through **CSC Corporate Domains, Inc.** with creation date **1995‑06‑05** and expiration **2027‑12‑08** (WHOIS).  
- Authoritative name servers: **ns.icann.org**, **a.iana-servers.net**, **b.iana-servers.net**, **c.iana-servers.net** (WHOIS/DNS NS).  
- Resolves to **IPv4 192.0.43.8** and **IPv6 2001:500:88:200::8** (DNS A/AAAA).  
- Mail exchangers are four ICANN hosts (pechora1‑8.icann.org) all with priority 10 (DNS MX).  
- DNS TXT records contain a variety of verification strings (OpenAI, Smartsheet, Microsoft, Google, Yahoo, Docusign, HaveIBeenPwned, SPF redirect to icann.org) (DNS TXT).  

## Notable findings
- Shodan reports the host **192.0.43.8** as running **Apache HTTP Server** and listening on ports **21 (FTP), 80 (HTTP), 443 (HTTPS)** (Shodan).  
- Hostnames observed by Shodan: **43-8.any.icann.org** and **iana.org** (Shodan).  
- Wayback Machine shows the earliest archived snapshot on **1997‑12‑10**, with the most recent listed snapshot **2005‑02‑06**, totaling **200** captures (Wayback).  

## Open questions
- No evidence in the provided data about current web content, services beyond the listed ports, or recent Wayback snapshots after 2005.  
- The purpose of the numerous verification TXT records (e.g., OpenAI, Smartsheet, Google) is unclear without further context.  
- No information on TLS certificates, CDN usage, or any recent infrastructure changes is available in the evidence set.

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 7 |
| DNS | 1 | 20 |
| Shodan IDB | 1 | 6 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 3 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `CSC Corporate Domains, Inc.` | WHOIS |
| 2 | whois | creation_date | `1995-06-05` | WHOIS |
| 3 | whois | expiration_date | `2027-12-08` | WHOIS |
| 4 | whois | name_server | `ns.icann.org` | WHOIS |
| 5 | whois | name_server | `a.iana-servers.net` | WHOIS |
| 6 | whois | name_server | `b.iana-servers.net` | WHOIS |
| 7 | whois | name_server | `c.iana-servers.net` | WHOIS |
| 8 | dns | dns.a | `192.0.43.8` | DNS A |
| 9 | dns | dns.aaaa | `2001:500:88:200::8` | DNS AAAA |
| 10 | dns | dns.mx | `10 pechora8.icann.org.` | DNS MX |
| 11 | dns | dns.mx | `10 pechora6.icann.org.` | DNS MX |
| 12 | dns | dns.mx | `10 pechora1.icann.org.` | DNS MX |
| 13 | dns | dns.mx | `10 pechora7.icann.org.` | DNS MX |
| 14 | dns | dns.ns | `a.iana-servers.net.` | DNS NS |
| 15 | dns | dns.ns | `ns.icann.org.` | DNS NS |
| 16 | dns | dns.ns | `c.iana-servers.net.` | DNS NS |
| 17 | dns | dns.ns | `b.iana-servers.net.` | DNS NS |
| 18 | dns | dns.txt | `openai-domain-verification=dv-PthFCD7xcAsc4Af2tmFj9sui` | DNS TXT |
| 19 | dns | dns.txt | `smartsheet-site-validation=CcnvONgQ2ibuzf2zHZxgPaWUqTwt-Sjr` | DNS TXT |
| 20 | dns | dns.txt | `MS=ms22660639` | DNS TXT |
| 21 | dns | dns.txt | `google-site-verification=iIqTTcUxND4wZOeVe5Ho728rH3JOSDnssYsYJ7pUtQQ` | DNS TXT |
| 22 | dns | dns.txt | `hibp-verify=dweb_deeci9b66kmruhrzqi0rgz1m` | DNS TXT |
| 23 | dns | dns.txt | `c9e864a6c53444038d34fe3a22513b74` | DNS TXT |
| 24 | dns | dns.txt | `docusign=b2d7c7b0-4627-494b-a7aa-682ee87c265d` | DNS TXT |
| 25 | dns | dns.txt | `v=spf1 redirect=icann.org` | DNS TXT |
| 26 | dns | dns.txt | `yahoo-verification-key=a1BzYfCAaz0f0Lu5ciZqvFkN93BwOIFipV9hvjjvqJw=` | DNS TXT |
| 27 | dns | dns.txt | `google-site-verification=6UylNQOBC9EN1ZNfySQ3g8XdRBqkGG4gifrzF9zsPD0` | DNS TXT |
| 28 | shodan | open_port | `21` | https://internetdb.shodan.io/192.0.43.8 |
| 29 | shodan | open_port | `80` | https://internetdb.shodan.io/192.0.43.8 |
| 30 | shodan | open_port | `443` | https://internetdb.shodan.io/192.0.43.8 |
| 31 | shodan | hostname | `43-8.any.icann.org` | https://internetdb.shodan.io/192.0.43.8 |
| 32 | shodan | hostname | `iana.org` | https://internetdb.shodan.io/192.0.43.8 |
| 33 | shodan | cpe | `cpe:/a:apache:http_server` | https://internetdb.shodan.io/192.0.43.8 |
| 34 | wayback | wayback.first_snapshot | `1997-12-10` | https://web.archive.org/web/19971210061738/http://www.iana.org:80/ |
| 35 | wayback | wayback.last_snapshot | `2005-02-06` | https://web.archive.org/web/20050206094755/http://www.iana.org:80/ |
| 36 | wayback | wayback.snapshot_count | `200` | http://web.archive.org/cdx/search/cdx |

## Trace

- plan: First run whois on iana.org to capture registrar, creation/expiry dates and name‑server details, establishing ownership and infrastructure baseline. Next query DNS for A/AAAA, MX, NS, TXT and CNAME records to map the live services, mail routing and any hidden subdomains. Then pull Shodan InternetDB data to see open ports, hostnames and known vulnerabilities tied to those IPs. After that search GitHub with code‑search dorks for “iana.org” to find accidental credential or config leaks. Finally review the Wayback Machine for historical snapshots, tracking changes in site structure, subdomains and exposed information over time.
- decide -> whois: Start with the cheapest tool to gather registration and ownership details for iana.org
- observe: whois: 7 findings (7 new), elapsed 926 ms
- decide -> dns: Gather A/AAAA, MX, NS, TXT, and CNAME records to map live services and subdomains
- observe: dns: 20 findings (20 new), elapsed 1536 ms
- decide -> shodan: Gather open ports, hostnames and vulnerability data for iana.org's IPs
- observe: shodan: 6 findings (6 new), elapsed 780 ms
- decide -> github: Search GitHub for iana.org references to uncover potential code or credential leaks
- observe: github: 0 findings (0 new), elapsed 413 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Cover the remaining tool to gather historical snapshots of iana.org
- observe: wayback: 3 findings (3 new), elapsed 14539 ms
- decide -> stop: All tools have been used and evidence gathered
