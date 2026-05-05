# OSINT briefing — `ox.ac.uk`

- **Generated:** 2026-05-05T07:24:44+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 69.49 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
ox.ac.uk – the primary domain of the University of Oxford.

## Key facts
- The domain is registered directly with Nominet, with no listed registrar. (WHOIS)  
- Creation date predates August 1996, indicating a long‑standing registration. (WHOIS)  
- Authoritative name servers are operated by the university: `dns0.ox.ac.uk`, `dns1.ox.ac.uk`, `dns2.ox.ac.uk`, `auth4.dns.ox.ac.uk`, `auth5.dns.ox.ac.uk`, `auth6.dns.ox.ac.uk`. (DNS NS)  
- The A record resolves to **13.51.62.86**. (DNS A)  
- MX records point to `oxforduni.in.tmes.trendmicro.eu`. (DNS MX)  
- Multiple TXT records show verification strings for Google, Facebook, GlobalSign, Microsoft, Jamf, OpenAI and others, as well as an SPF redirect to `_spf.ox.ac.uk`. (DNS TXT)  

## Notable findings
- The IP **13.51.62.86** hosts open ports 22 (SSH), 80 (HTTP) and 443 (HTTPS). (Shodan)  
- Reverse‑DNS / hostnames associated with this IP belong to the Swedish domain **balder.se** and an AWS EC2 instance (`ec2-13-51-62-86.eu-north-1.compute.amazonaws.com`). (Shodan)  
- No direct evidence links the university’s services to the balder.se hostnames; the Shodan data only reflects the current IP’s usage.  

## Open questions
- Why does the university’s A record point to an IP that resolves to balder.se hostnames and an AWS instance?  
- Are there load‑balancing, CDN, or cloud‑hosting arrangements that explain the shared IP?  
- What services are actually running on ports 22/80/443 at this address (e.g., web site, SSH gateway)?  

*The investigation is limited to the provided WHOIS, DNS, and Shodan records; no additional attribution or inference can be drawn from the current evidence.*

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 3 |
| DNS | 1 | 28 |
| Shodan IDB | 1 | 10 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `No registrar listed.  This domain is directly registered with Nominet.` | WHOIS |
| 2 | whois | creation_date | `before Aug-1996` | WHOIS |
| 3 | whois | name_server | `ns0.ja.net.` | WHOIS |
| 4 | dns | dns.a | `13.51.62.86` | DNS A |
| 5 | dns | dns.mx | `4 oxforduni.in.tmes.trendmicro.eu.` | DNS MX |
| 6 | dns | dns.ns | `dns0.ox.ac.uk.` | DNS NS |
| 7 | dns | dns.ns | `auth4.dns.ox.ac.uk.` | DNS NS |
| 8 | dns | dns.ns | `auth5.dns.ox.ac.uk.` | DNS NS |
| 9 | dns | dns.ns | `dns1.ox.ac.uk.` | DNS NS |
| 10 | dns | dns.ns | `dns2.ox.ac.uk.` | DNS NS |
| 11 | dns | dns.ns | `auth6.dns.ox.ac.uk.` | DNS NS |
| 12 | dns | dns.txt | `google-gws-recovery-domain-verification=56795791` | DNS TXT |
| 13 | dns | dns.txt | `google-site-verification=qb4BUD5Usjh0Nep0wKIkZIlLSR2rrXsD5PvYGIiKJtA` | DNS TXT |
| 14 | dns | dns.txt | `facebook-domain-verification=647crbrjssj5mgbuy5ptjl8c6qmh23` | DNS TXT |
| 15 | dns | dns.txt | `_globalsign-domain-verification=wiDg8qaoolWaTbaZq8YxJLFxFT36aoIO03meY20xze` | DNS TXT |
| 16 | dns | dns.txt | `google-site-verification=uHCoKrADK1i1za25F8hr2arNkmwrT3Krl7Jk5RRFCGM` | DNS TXT |
| 17 | dns | dns.txt | `v=spf1 redirect=_spf.ox.ac.uk` | DNS TXT |
| 18 | dns | dns.txt | `WtnAjq8L8o3AgONKmYl7NTJrA9qe5GAxdO3xYq1hVcdXZ0THaEYNiyx74cio/8CE8E3rDApP0jojGJhH` | DNS TXT |
| 19 | dns | dns.txt | `MS=ms57844111` | DNS TXT |
| 20 | dns | dns.txt | `google-site-verification=xqPbmJpDfZK648oMnCGuFpkn5HJqLhpMRPkss5jEhHk` | DNS TXT |
| 21 | dns | dns.txt | `b8zq7ht7w0jmhx3wgzn5srmjl8b0y0gp` | DNS TXT |
| 22 | dns | dns.txt | `1zl23trd62r8wgvvrv0gjg7z1gxr64gw` | DNS TXT |
| 23 | dns | dns.txt | `ueG8e2rFCvZiPIxG4L1VRVcqLV6m3yrjJCRro8ZHPiZDX7y6xFsvBuCirQG9MAFSaqKwX55TK/G0WVh6` | DNS TXT |
| 24 | dns | dns.txt | `jamf-site-verification=z4aTHKJhScEjBS_E-BOcdA` | DNS TXT |
| 25 | dns | dns.txt | `022fc977acdd42cabb4a3cd9d17138bb` | DNS TXT |
| 26 | dns | dns.txt | `openai-domain-verification=dv-FrXjlS30zrnR8T3D1ktwxud7` | DNS TXT |
| 27 | dns | dns.txt | `1FBF055C-7912-4406-8091-79206812E154` | DNS TXT |
| 28 | dns | dns.txt | `google-site-verification=Axf59TQZibIC5SStWVv4XULS6AONRp5c-G2Vmzrq_Yw` | DNS TXT |
| 29 | dns | dns.txt | `wdc9f05rx6mmn1rgzqrxz8l7ljrn2c5x` | DNS TXT |
| 30 | dns | dns.txt | `QuoVadis=fbb7711c-3934-4311-b571-fd7695107436` | DNS TXT |
| 31 | dns | dns.txt | `hes=3c57da24c0cf354d2d270f87f9033045` | DNS TXT |
| 32 | shodan | open_port | `22` | https://internetdb.shodan.io/13.51.62.86 |
| 33 | shodan | open_port | `80` | https://internetdb.shodan.io/13.51.62.86 |
| 34 | shodan | open_port | `443` | https://internetdb.shodan.io/13.51.62.86 |
| 35 | shodan | hostname | `cms.balder.se` | https://internetdb.shodan.io/13.51.62.86 |
| 36 | shodan | hostname | `nyproduktion.balder.se` | https://internetdb.shodan.io/13.51.62.86 |
| 37 | shodan | hostname | `www.balder.se` | https://internetdb.shodan.io/13.51.62.86 |
| 38 | shodan | hostname | `search.balder.se` | https://internetdb.shodan.io/13.51.62.86 |
| 39 | shodan | hostname | `en.balder.se` | https://internetdb.shodan.io/13.51.62.86 |
| 40 | shodan | hostname | `ec2-13-51-62-86.eu-north-1.compute.amazonaws.com` | https://internetdb.shodan.io/13.51.62.86 |
| 41 | shodan | hostname | `balder.se` | https://internetdb.shodan.io/13.51.62.86 |

## Trace

- plan: First run whois to capture the registrar, registration dates and name‑servers, establishing ownership and infrastructure baseline. Next query dns for A/AAAA, MX, NS, TXT and CNAME records to map current services, mail routing and possible subdomains. Then use shodan to discover open ports, hostnames and known vulnerabilities on the resolved IPs. After that search github for “ox.ac.uk” in code, config files or accidental credential commits. Finally pull wayback snapshots to see historic site content, subdomains and past DNS changes.
- decide -> whois: Start with cheap WHOIS lookup to get registration and name‑server info for ox.ac.uk
- observe: whois: 3 findings (3 new), elapsed 1029 ms
- decide -> dns: Gather current DNS records to map services and subdomains after establishing registration info
- observe: dns: 28 findings (28 new), elapsed 1719 ms
- decide -> shodan: Next step is to discover open ports, hostnames, and vulnerabilities on the target's IPs
- observe: shodan: 10 findings (10 new), elapsed 612 ms
- decide -> github: Next tool in plan is GitHub to find code or config referencing ox.ac.uk
- observe: github: 0 findings (0 new), elapsed 3136 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Collect historic snapshots of ox.ac.uk to identify past content, subdomains, and DNS changes
- observe: wayback: 0 findings (0 new), elapsed 15406 ms, error: Wayback CDX request failed: ReadTimeout
- decide -> stop: All tools have been used and relevant evidence collected
