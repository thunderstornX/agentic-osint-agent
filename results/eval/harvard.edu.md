# OSINT briefing — `harvard.edu`

- **Generated:** 2026-05-05T07:22:24+00:00
- **Provider / model:** `openrouter` / `openai/gpt-oss-120b:free`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 67.44 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
**harvard.edu** – primary domain of Harvard University.

## Key facts
- The authoritative A record resolves to **192.0.66.20** (dns)【dns】.  
- Shodan reports this IP hosts **HTTP (80)** and **HTTPS (443)** services, identified as **nginx** (cpe:/a:f5:nginx)【shodan】.  
- Hostnames associated with the IP are **harvard.edu** and **www.harvard.edu**【shodan】.  
- MX records point to **mx0a-00171101.pphosted.com** and **mx0b-00171101.pphosted.com** (both priority 100)【dns】.  
- Nameservers are a set of Akamai edge servers (a1‑171.akam.net, a6‑66.akam.net, a7‑65.akam.net, a10‑66.akam.net, a11‑67.akam.net, a16‑64.akam.net)【dns】.  
- Numerous TXT records exist for verification with third‑party services (Google, Atlassian, OpenAI, Anthropic, Airtable, Fastly, Heroku, Jamf, Adobe, Cisco, etc.)【dns】. No single TXT record reveals additional infrastructure details.

## Notable findings
- The presence of **Akamai** nameservers indicates that Harvard’s web traffic is likely CDN‑accelerated.  
- The **nginx** banner on port 443 suggests a reverse‑proxy or load‑balancer front‑ending the site.  
- The extensive list of verification TXT records shows active integration with many SaaS platforms (e.g., Google Workspace, Atlassian, OpenAI, Anthropic, Fastly, Heroku). This reflects a broad ecosystem of cloud services tied to the domain.

## Open questions
- Which specific services (e.g., mail, analytics, CI/CD) correspond to the numerous verification TXT entries?  
- Are there additional IP addresses behind the CDN that host other Harvard subdomains or services?  
- What is the exact configuration of the nginx instance (version, modules) beyond the generic CPE tag?  
- Are any of the verification tokens still valid, indicating active contracts with the listed providers?  

*No further evidence is available beyond the DNS and Shodan records listed.*

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 0 |
| DNS | 1 | 57 |
| Shodan IDB | 1 | 5 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | dns | dns.a | `192.0.66.20` | DNS A |
| 2 | dns | dns.mx | `100 mx0a-00171101.pphosted.com.` | DNS MX |
| 3 | dns | dns.mx | `100 mx0b-00171101.pphosted.com.` | DNS MX |
| 4 | dns | dns.ns | `a10-66.akam.net.` | DNS NS |
| 5 | dns | dns.ns | `a11-67.akam.net.` | DNS NS |
| 6 | dns | dns.ns | `a16-64.akam.net.` | DNS NS |
| 7 | dns | dns.ns | `a6-66.akam.net.` | DNS NS |
| 8 | dns | dns.ns | `a1-171.akam.net.` | DNS NS |
| 9 | dns | dns.ns | `a7-65.akam.net.` | DNS NS |
| 10 | dns | dns.txt | `status-page-domain-verification=b4j4g69th3vv` | DNS TXT |
| 11 | dns | dns.txt | `smartsheet-site-validation=jfLh_IkQNJXuKKpTn7RydwiiaAOLy4CR` | DNS TXT |
| 12 | dns | dns.txt | `v=spf1 include:%{i}._ip.%{h}._ehlo.%{d}._spf.vali.email ~all` | DNS TXT |
| 13 | dns | dns.txt | `airtable-verification=b25f432db3cbc5bfc481914364b6ce41` | DNS TXT |
| 14 | dns | dns.txt | `google-site-verification=DZTZhbBaYJ6AO5j-tHFYBdkwryNywFh2gMUeg3SRDSg` | DNS TXT |
| 15 | dns | dns.txt | `globalsign-domain-verification=87677a19ae97bfbeec25ff1510a80420` | DNS TXT |
| 16 | dns | dns.txt | `globalsign-domain-verification=1C94E0FFAAE95796F597427644D90C03` | DNS TXT |
| 17 | dns | dns.txt | `brevo-code:30d9f789747b4c124f72dabf24a0a97f` | DNS TXT |
| 18 | dns | dns.txt | `google-site-verification=lY-T8NneGQX1RGXeaoBJjSmT_lx3dLRKDq1xY44ZI5w` | DNS TXT |
| 19 | dns | dns.txt | `google-site-verification=NEWpTHNZnWRWN3trkIMeFbuPVG3ExwOXUHlC9aJ2sks` | DNS TXT |
| 20 | dns | dns.txt | `_51a79b140kb1cu9o67nzuefyhhxthv9` | DNS TXT |
| 21 | dns | dns.txt | `globalsign-domain-verification=C44DEEAC45AB4DC2B5AD0B9B2E5D5803` | DNS TXT |
| 22 | dns | dns.txt | `openai-domain-verification=dv-5z82SztO32q9YBNgFooNBz5v` | DNS TXT |
| 23 | dns | dns.txt | `_cwe6cxmi9tji7gazwtzipl4onpu23nv` | DNS TXT |
| 24 | dns | dns.txt | `anthropic-domain-verification-gy5zhc=zmrGT2kyyc2HlnUn6f0utkQB6` | DNS TXT |
| 25 | dns | dns.txt | `atlassian-domain-verification=Z8oUd5brL6/RGUMCkxs4U0P/RyhpiNJEIVx9HXJLr3uqEQ1eDm` | DNS TXT |
| 26 | dns | dns.txt | `ciscocidomainverification=41ce9827e3fbbca9ce75d5dbb5a6bc7b089dc4e239c1b56ba82821` | DNS TXT |
| 27 | dns | dns.txt | `airtable-verification=a92cef30671587a4f6deb7951c1c3f1a` | DNS TXT |
| 28 | dns | dns.txt | `fastly-domain-delgation-vdnblsdg768nm-21052021` | DNS TXT |
| 29 | dns | dns.txt | `atlassian-domain-verification=ASRKBXyOafZgDCRWh1Ylv34hiOSMgAIoNXs8H57rR3aTkuOD5K` | DNS TXT |
| 30 | dns | dns.txt | `pardot679353=3cc5e124c5020a1e160f01981f45be33a467a1c802711e0e5654184ef56d18c9` | DNS TXT |
| 31 | dns | dns.txt | `heroku-domain-verification=1qfmzz9vp3kexf4fr5zuliwvpieih2ffz4gexo7tlh4` | DNS TXT |
| 32 | dns | dns.txt | `globalsign-domain-verification=B8359DCEFBCF837B95E2F82282E4297A` | DNS TXT |
| 33 | dns | dns.txt | `jamf-site-verification=3o6gdpul8xpeqY0GpAZqxw` | DNS TXT |
| 34 | dns | dns.txt | `adobe-idp-site-verification=66e813947c764d98330002232f383a68df8ad609065abb9482f3` | DNS TXT |
| 35 | dns | dns.txt | `openai-domain-verification=dv-e8vYSnmmPbWxpNte1iIKgvOO` | DNS TXT |
| 36 | dns | dns.txt | `globalsign-domain-verification=9ff12eafbeebb02a0f2b0383aef9d1fa` | DNS TXT |
| 37 | dns | dns.txt | `globalsign-domain-verification=5A1F4E0081852ECB9015E837384121AD` | DNS TXT |
| 38 | dns | dns.txt | `atlassian-domain-verification=OYfkFwspEELRW6A32BsDVWgvdz8/pLBxVcq7s/mHLBVGqRQRG5` | DNS TXT |
| 39 | dns | dns.txt | `xIGeuA0e5B1BOjTE4IBO806ziFX9G1m2dVJ8zO7CMkmKwZ6MEkMXC0P7n5SRCGOdS9jbceH/7gKYgD4h` | DNS TXT |
| 40 | dns | dns.txt | `google-site-verification=MmfJS0BjLRgcxrlj8kAyNdToKeAmj0fKb-lPOnd5Pmo` | DNS TXT |
| 41 | dns | dns.txt | `google-site-verification=pWvLuNePLYxAbafZw2a95vnBhvcj12DzM9NulT9ujSY` | DNS TXT |
| 42 | dns | dns.txt | `airtable-verification=8b8110e9283dd87d57b3c5f2f5af2db1` | DNS TXT |
| 43 | dns | dns.txt | `status-page-domain-verification=p83gt91wpxms` | DNS TXT |
| 44 | dns | dns.txt | `jAykGnWytyLeBseMa8x2/MBve6/yQqana4yrAc1ROoei7uZHUkM2FU0Xx4qI/rm+kOGdImZdoq0fdodg` | DNS TXT |
| 45 | dns | dns.txt | `geneious.com:domain-verification=1781B6exIEsRBzJ0KzPtKg` | DNS TXT |
| 46 | dns | dns.txt | `globalsign-domain-verification=1DDF777ED1ADF45E5FFAFFAAD6774180` | DNS TXT |
| 47 | dns | dns.txt | `globalsign-domain-verification=dcc2e5d0d67efc32044ae679c7cf19e6` | DNS TXT |
| 48 | dns | dns.txt | `google-site-verification=DzhZyP8pu0M1-RFghfTcSN-9poidboYRNdfn2Rf2hCQ` | DNS TXT |
| 49 | dns | dns.txt | `pardot_378242_*=8b485d5cd9114869cff8f307da5fa9287434ebec11621d88c07ce97a7fee06e0` | DNS TXT |
| 50 | dns | dns.txt | `google-site-verification=xXWxVElKH8ek_eW45CbAqVSMTQgAqLYUNQUrWpOmkrY` | DNS TXT |
| 51 | dns | dns.txt | `anthropic-domain-verification-dprfjc=K9LyiFV7zLafnNLNO4lFjyaRx` | DNS TXT |
| 52 | dns | dns.txt | `pardot378242=7001579db574e062735763ba81b54da111abc31facf16bbfa653ab6b8a770988` | DNS TXT |
| 53 | dns | dns.txt | `google-site-verification=xqg8LPF_v_QMEIST789q8xhRDqUEX4_8lQjAvV6YykY` | DNS TXT |
| 54 | dns | dns.txt | `MS=ms35192554` | DNS TXT |
| 55 | dns | dns.txt | `Peh2GHoW8uiAzwS9tTZKlGBn9cMq6Y+XUFtrqmLtqFh1WvloPkzGczPsZcSdDfin4hZ7QiL9J7SM8yr7` | DNS TXT |
| 56 | dns | dns.txt | `pardot962443=9098884472c5cb29a2e20700b41411cb4aa5ebcf340360e71b2cd8464d8864b6` | DNS TXT |
| 57 | dns | dns.txt | `pardot679353=f93ea3588d69483bf48dbf587511f51d43ddadaae52b8bac6856c8428559a06d` | DNS TXT |
| 58 | shodan | open_port | `80` | https://internetdb.shodan.io/192.0.66.20 |
| 59 | shodan | open_port | `443` | https://internetdb.shodan.io/192.0.66.20 |
| 60 | shodan | hostname | `www.harvard.edu` | https://internetdb.shodan.io/192.0.66.20 |
| 61 | shodan | hostname | `harvard.edu` | https://internetdb.shodan.io/192.0.66.20 |
| 62 | shodan | cpe | `cpe:/a:f5:nginx` | https://internetdb.shodan.io/192.0.66.20 |

## Trace

- plan: First run whois to capture registrar details, creation/expiry dates and name‑servers, establishing ownership and infrastructure age. Next query dns for A/AAAA, MX, NS, TXT and CNAME records to map hosts, mail routing, subdomains and possible misconfigurations. Then use shodan to enumerate open ports, services, hostnames and known vulnerabilities tied to those IPs. After that search github for “harvard.edu” code‑dorks to find accidental credential or config leaks. Finally pull wayback snapshots to see historic site structure, subdomains and content changes that may reveal legacy assets.
- decide -> whois: Start with the cheapest tool to gather ownership and registrar information for harvard.edu
- observe: whois: 0 findings (0 new), elapsed 529 ms
- decide -> dns: Next cheap tool to map IPs, MX, NS, and subdomains for harvard.edu
- observe: dns: 57 findings (57 new), elapsed 1158 ms
- decide -> shodan: Next step is to enumerate open ports, services, and host details for harvard.edu IPs
- observe: shodan: 5 findings (5 new), elapsed 544 ms
- decide -> github: Next tool in plan to search for harvard.edu code leaks
- observe: github: 0 findings (0 new), elapsed 3419 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: Cover the remaining tool to gather historic site data and subdomains
- observe: wayback: 0 findings (0 new), elapsed 15431 ms, error: Wayback CDX request failed: ReadTimeout
- decide -> stop: All tools have been used and evidence gathered
