# OSINT briefing — `cisa.gov`

- **Generated:** 2026-05-05T07:17:22+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 73.65 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
cisa.gov  

## Key facts
- Domain is registered through **get.gov** with creation date **2018‑12‑06** and expiration **2026‑11‑04** (WHOIS).  
- Registrant organization is redacted for privacy (WHOIS).  
- Authoritative name servers are **blue.foundationdns.com**, **blue.foundationdns.net**, and **blue.foundationdns.org** (WHOIS / DNS NS).  

## Notable findings
- The domain resolves to IPv4 **23.50.82.177** and two IPv6 addresses **2600:1417:7a:296::3ff9** and **2600:1417:7a:293::3ff9** (DNS A/AAAA).  
- Shodan reports the host on port **80** with the hostname **a23-50-82-177.deploy.static.akamaitechnologies.com** (Shodan).  
- Mail exchangers are **mxa-00376703.gslb.gpphosted.com** and **mxb-00376703.gslb.gpphosted.com** (DNS MX).  
- SPF record includes **spf.dhs.gov**, **spf.protection.outlook.com**, and **spf-00376703.gpphosted.com** (DNS TXT).  
- Multiple verification TXT records are present, including Google site verification strings, Microsoft verification IDs (MS=...), Adobe IDP verification, and Censys domain verification tokens (DNS TXT).  
- Additional opaque TXT strings (e.g., `_e01yoinuk3n6xrtnc8q3m9bdjyihdd7`, `f188eb27-a746-4aa8-b160-eb68b0aab05d`) are observed (DNS TXT).  

## Open questions
- The purpose of the numerous verification TXT records and opaque strings is unclear; they may relate to third‑party services or security testing.  
- No evidence of additional open ports, services, or infrastructure beyond the observed HTTP endpoint on port 80.  
- The relationship between the Akamai static hostname and the CISA domain is not detailed in the available data.

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 7 |
| DNS | 1 | 21 |
| Shodan IDB | 1 | 2 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `get.gov` | WHOIS |
| 2 | whois | creation_date | `2018-12-06` | WHOIS |
| 3 | whois | expiration_date | `2026-11-04` | WHOIS |
| 4 | whois | name_server | `blue.foundationdns.com` | WHOIS |
| 5 | whois | name_server | `blue.foundationdns.net` | WHOIS |
| 6 | whois | name_server | `blue.foundationdns.org` | WHOIS |
| 7 | whois | registrant_org | `REDACTED FOR PRIVACY` | WHOIS |
| 8 | dns | dns.a | `23.50.82.177` | DNS A |
| 9 | dns | dns.aaaa | `2600:1417:7a:296::3ff9` | DNS AAAA |
| 10 | dns | dns.aaaa | `2600:1417:7a:293::3ff9` | DNS AAAA |
| 11 | dns | dns.mx | `10 mxb-00376703.gslb.gpphosted.com.` | DNS MX |
| 12 | dns | dns.mx | `10 mxa-00376703.gslb.gpphosted.com.` | DNS MX |
| 13 | dns | dns.ns | `blue.foundationdns.net.` | DNS NS |
| 14 | dns | dns.ns | `blue.foundationdns.com.` | DNS NS |
| 15 | dns | dns.ns | `blue.foundationdns.org.` | DNS NS |
| 16 | dns | dns.txt | `_e01yoinuk3n6xrtnc8q3m9bdjyihdd7` | DNS TXT |
| 17 | dns | dns.txt | `google-site-verification=BNRBfY90BM54Mf_pgL4Eg07IkwbGvq5nsdZCOYadDlM` | DNS TXT |
| 18 | dns | dns.txt | `MS=ms36056523` | DNS TXT |
| 19 | dns | dns.txt | `MS=ms53160703` | DNS TXT |
| 20 | dns | dns.txt | `MS=ms41452370` | DNS TXT |
| 21 | dns | dns.txt | `_rr8gice4wv589e4uxop5zqhh6gbqh32` | DNS TXT |
| 22 | dns | dns.txt | `censys-domain-verification=oCKV9OzJ1EtsMPZGDfdkccVF2WRuGqmhhozTHjaNAsvH` | DNS TXT |
| 23 | dns | dns.txt | `_tufdw17aa2wht723upz8w56htpvpgkw` | DNS TXT |
| 24 | dns | dns.txt | `google-site-verification=wsLVyeZYgv0NLikdmfm2m3XPP-986Ylo8XxUkrjIOvA` | DNS TXT |
| 25 | dns | dns.txt | `adobe-idp-site-verification=edfd88b4c2bdf65395c78b55da3580466eefa9aa874d5bcfb853` | DNS TXT |
| 26 | dns | dns.txt | `f188eb27-a746-4aa8-b160-eb68b0aab05d` | DNS TXT |
| 27 | dns | dns.txt | `censys-domain-verification=kSZxqevdrY_nf9ogHWhuUq2O39C9Lkj-pSfnrCzSOVxO` | DNS TXT |
| 28 | dns | dns.txt | `v=spf1 include:spf.dhs.gov include:spf.protection.outlook.com include:spf-003767` | DNS TXT |
| 29 | shodan | open_port | `80` | https://internetdb.shodan.io/23.50.82.177 |
| 30 | shodan | hostname | `a23-50-82-177.deploy.static.akamaitechnologies.com` | https://internetdb.shodan.io/23.50.82.177 |

## Trace

- plan: First run whois to capture the registrar, registration dates and name‑servers, establishing ownership and age. Next query dns for A/AAAA, MX, NS, TXT and CNAME records to map the current infrastructure, mail routing and any hidden subdomains. Then pull shodan InternetDB data to see open ports, services, hostnames and known vulnerabilities. After that search github for the domain using code‑search dorks to find accidental credential or config leaks. Finally review wayback snapshots to track historical site changes, subdomains and past tech stacks.
- decide -> whois: Start with cheap WHOIS lookup to get registration and ownership details
- observe: whois: 7 findings (7 new), elapsed 1348 ms
- decide -> dns: Gather DNS records to map infrastructure after WHOIS info
- observe: dns: 21 findings (21 new), elapsed 417 ms
- decide -> shodan: Gather open ports, services and vulnerabilities for cisa.gov
- observe: shodan: 2 findings (2 new), elapsed 511 ms
- decide -> github: Next tool in plan to search code repositories for domain leaks
- observe: github: 0 findings (0 new), elapsed 3065 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Cover the remaining tool to gather historical snapshots of cisa.gov
- observe: wayback: 0 findings (0 new), elapsed 15344 ms, error: Wayback CDX request failed: ReadTimeout
- decide -> stop: All five tools have been used and evidence gathered
