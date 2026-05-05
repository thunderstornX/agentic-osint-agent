# OSINT briefing — `torproject.org`

- **Generated:** 2026-05-05T07:31:40+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 66.86 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target  
**torproject.org** – the primary domain of the Tor Project.

## Key facts  
- The domain was registered on **2006‑10‑17** and is set to expire on **2027‑10‑17** (WHOIS).  
- Registrar: **CSL Computer Service Langenbach GmbH d/b/a joker.com** (WHOIS).  
- Authoritative name servers listed in WHOIS and DNS records include **ns1‑ns5.torproject.org** and **nsp.dnsnode.net** (WHOIS, DNS NS).  
- MX record points to **mx‑dal‑01.torproject.org** (DNS MX).  
- DNS TXT records contain a Google site‑verification token, an SPF policy referencing several internal hosts, and an opaque token string (DNS TXT).  

## Notable findings  
- Multiple A records resolve the domain to IPv4 addresses **204.8.99.144**, **204.8.99.146**, **95.216.163.36**, **116.202.120.165**, and **116.202.120.166** (DNS A).  
- IPv6 AAAA records include **2620:7:6002:0:466:39ff:fe7f:1826**, **2620:7:6002:0:466:39ff:fe32:e3dd**, **2a01:4f9:c010:19eb::1**, **2a01:4f8:fff0:4f:266:37ff:fe2c:5d19**, and **2a01:4f8:fff0:4f:266:37ff:feae:3bbc** (DNS AAAA).  
- Shodan data for IP **116.202.120.166** shows open HTTP (80) and HTTPS (443) ports, hostnames **torproject.org** and **web-fsn-02.torproject.org**, and identifies the service as **Apache HTTP Server** (Shodan).  

## Open questions  
- The purpose and ownership of the additional A records (e.g., 204.8.99.144/146, 95.216.163.36) are not clarified by the available evidence.  
- No information is provided about the content or configuration of the Apache server observed on port 80/443.  
- The meaning of the opaque DNS TXT token (`_dpwm8776gpzbj9ttd4teweyhomh2ove`) remains unknown.  

*All statements are directly derived from the supplied WHOIS, DNS, and Shodan evidence.*

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 9 |
| DNS | 1 | 20 |
| Shodan IDB | 1 | 5 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `CSL Computer Service Langenbach GmbH d/b/a joker.com` | WHOIS |
| 2 | whois | creation_date | `2006-10-17` | WHOIS |
| 3 | whois | expiration_date | `2027-10-17` | WHOIS |
| 4 | whois | name_server | `ns4.torproject.org` | WHOIS |
| 5 | whois | name_server | `ns5.torproject.org` | WHOIS |
| 6 | whois | name_server | `ns1.torproject.org` | WHOIS |
| 7 | whois | name_server | `ns3.torproject.org` | WHOIS |
| 8 | whois | name_server | `nsp.dnsnode.net` | WHOIS |
| 9 | whois | name_server | `ns2.torproject.org` | WHOIS |
| 10 | dns | dns.a | `204.8.99.144` | DNS A |
| 11 | dns | dns.a | `95.216.163.36` | DNS A |
| 12 | dns | dns.a | `116.202.120.165` | DNS A |
| 13 | dns | dns.a | `116.202.120.166` | DNS A |
| 14 | dns | dns.a | `204.8.99.146` | DNS A |
| 15 | dns | dns.aaaa | `2620:7:6002:0:466:39ff:fe7f:1826` | DNS AAAA |
| 16 | dns | dns.aaaa | `2a01:4f9:c010:19eb::1` | DNS AAAA |
| 17 | dns | dns.aaaa | `2620:7:6002:0:466:39ff:fe32:e3dd` | DNS AAAA |
| 18 | dns | dns.aaaa | `2a01:4f8:fff0:4f:266:37ff:fe2c:5d19` | DNS AAAA |
| 19 | dns | dns.aaaa | `2a01:4f8:fff0:4f:266:37ff:feae:3bbc` | DNS AAAA |
| 20 | dns | dns.mx | `10 mx-dal-01.torproject.org.` | DNS MX |
| 21 | dns | dns.ns | `ns2.torproject.org.` | DNS NS |
| 22 | dns | dns.ns | `nsp.dnsnode.net.` | DNS NS |
| 23 | dns | dns.ns | `ns4.torproject.org.` | DNS NS |
| 24 | dns | dns.ns | `ns5.torproject.org.` | DNS NS |
| 25 | dns | dns.ns | `ns1.torproject.org.` | DNS NS |
| 26 | dns | dns.ns | `ns3.torproject.org.` | DNS NS |
| 27 | dns | dns.txt | `google-site-verification=YeQsuz0lo1q00m6KE1lpJX7hHBzriDpcMHr_f9q2Ag8` | DNS TXT |
| 28 | dns | dns.txt | `v=spf1 a:crm-int-01.torproject.org a:submit-01.torproject.org a:rdsys-frontend-0` | DNS TXT |
| 29 | dns | dns.txt | `_dpwm8776gpzbj9ttd4teweyhomh2ove` | DNS TXT |
| 30 | shodan | open_port | `80` | https://internetdb.shodan.io/116.202.120.166 |
| 31 | shodan | open_port | `443` | https://internetdb.shodan.io/116.202.120.166 |
| 32 | shodan | hostname | `torproject.org` | https://internetdb.shodan.io/116.202.120.166 |
| 33 | shodan | hostname | `web-fsn-02.torproject.org` | https://internetdb.shodan.io/116.202.120.166 |
| 34 | shodan | cpe | `cpe:/a:apache:http_server` | https://internetdb.shodan.io/116.202.120.166 |

## Trace

- plan: First run whois to capture registrar details, creation/expiry dates and name‑servers, establishing ownership and timeline. Next query dns for A/AAAA, MX, NS, TXT and CNAME records to map the current infrastructure, mail routing and any SPF/DKIM policies. Then pull shodan InternetDB data to see exposed ports, hostnames and known vulnerabilities. After that search github for “torproject.org” code‑dorks to find accidental credential or config leaks. Finally review wayback snapshots to track historical DNS, site changes and past exposed assets.
- decide -> whois: Start with cheap whois to get registrar and ownership details for torproject.org
- observe: whois: 9 findings (9 new), elapsed 615 ms
- decide -> dns: Gather current DNS records to map infrastructure after WHOIS info
- observe: dns: 20 findings (20 new), elapsed 744 ms
- decide -> shodan: Next step is to gather Internet-facing host data and open ports for torproject.org
- observe: shodan: 5 findings (5 new), elapsed 617 ms
- decide -> github: Search GitHub for torproject.org references to uncover potential code or credential leaks
- observe: github: 0 findings (0 new), elapsed 3155 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Cover the remaining tool to examine historical snapshots of torproject.org
- observe: wayback: 0 findings (0 new), elapsed 5715 ms, error: Wayback CDX returned HTTP 503
- decide -> stop: All five tools have been used and evidence gathered
