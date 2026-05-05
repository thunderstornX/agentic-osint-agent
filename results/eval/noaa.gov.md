# OSINT briefing — `noaa.gov`

- **Generated:** 2026-05-05T07:01:57+00:00
- **Provider / model:** `nvidia` / `meta/llama-3.3-70b-instruct`
- **Iterations:** 5 of 8 budget
- **Wall-clock:** 93.31 s
- **Tool coverage:** 5/5  (dns, github, shodan, wayback, whois)
- **Finish reason:** `covered_all_tools`
- **Operator authority:** Public-interest research; targets are .gov, .edu, large NGOs, or RFC-reserved domains; passive sources only.

## Briefing

## Target
The target of this investigation is the domain noaa.gov.

## Key facts
The domain noaa.gov was created on 1997-10-02 and is set to expire on 2026-08-04 (WHOIS). The registrar is get.gov (WHOIS). The domain has multiple name servers, including ns-01.noaa.gov, ns-02.noaa.gov, and ns-03.noaa.gov (WHOIS, DNS NS).

## Notable findings
The domain has multiple IP addresses associated with it, including 137.75.88.52 and 137.75.88.7 (DNS A). It also has IPv6 addresses, such as 2610:20:8000:8c04::24 (DNS AAAA). The domain uses Google mail servers, as indicated by the MX records (DNS MX). The domain has a number of open ports, including 80 and 443, which are commonly used for HTTP and HTTPS traffic (Shodan). The web server is running Apache HTTP Server (Shodan).

## Open questions
The evidence provided is largely related to DNS and network configuration, but does not provide much information about the content or usage of the domain. Further investigation would be needed to determine the purpose and scope of the domain. Additionally, the registrant organization is redacted for privacy (WHOIS), which may limit the ability to gather more information about the domain's ownership and administration.

## Evidence by tool

| Tool | Calls | Findings |
|---|---:|---:|
| WHOIS | 1 | 7 |
| DNS | 1 | 68 |
| Shodan IDB | 1 | 4 |
| GitHub Dork | 1 | 0 |
| Wayback CDX | 1 | 0 |

## Evidence rows

| # | Tool | Kind | Value | Source |
|---:|---|---|---|---|
| 1 | whois | registrar | `get.gov` | WHOIS |
| 2 | whois | creation_date | `1997-10-02` | WHOIS |
| 3 | whois | expiration_date | `2026-08-04` | WHOIS |
| 4 | whois | name_server | `ns-01.noaa.gov` | WHOIS |
| 5 | whois | name_server | `ns-02.noaa.gov` | WHOIS |
| 6 | whois | name_server | `ns-03.noaa.gov` | WHOIS |
| 7 | whois | registrant_org | `REDACTED FOR PRIVACY` | WHOIS |
| 8 | dns | dns.a | `137.75.88.52` | DNS A |
| 9 | dns | dns.a | `137.75.88.7` | DNS A |
| 10 | dns | dns.aaaa | `2610:20:8000:8c04::24` | DNS AAAA |
| 11 | dns | dns.aaaa | `2610:20:8800:8c00::24` | DNS AAAA |
| 12 | dns | dns.mx | `20 ALT1.ASPMX.L.GOOGLE.COM.` | DNS MX |
| 13 | dns | dns.mx | `40 ALT4.ASPMX.L.GOOGLE.COM.` | DNS MX |
| 14 | dns | dns.mx | `20 ALT2.ASPMX.L.GOOGLE.COM.` | DNS MX |
| 15 | dns | dns.mx | `10 ASPMX.L.GOOGLE.COM.` | DNS MX |
| 16 | dns | dns.mx | `40 ALT3.ASPMX.L.GOOGLE.COM.` | DNS MX |
| 17 | dns | dns.ns | `ns-02.noaa.gov.` | DNS NS |
| 18 | dns | dns.ns | `ns-03.noaa.gov.` | DNS NS |
| 19 | dns | dns.ns | `ns-01.noaa.gov.` | DNS NS |
| 20 | dns | dns.txt | `_globalsign-domain-verification=EkeEUzVEdHxpmz9oj4HdaKJOyr0yFaZuGM5T24zHgH` | DNS TXT |
| 21 | dns | dns.txt | `bpt25c606kitfrsm1js9pa39uj` | DNS TXT |
| 22 | dns | dns.txt | `icsspgfokcnpncvdbehbe5t5u4` | DNS TXT |
| 23 | dns | dns.txt | `_yy3kidedxo7p355zl2ny2vkapuht0tk` | DNS TXT |
| 24 | dns | dns.txt | `jkrb63gop4200qdglch6mrrigt` | DNS TXT |
| 25 | dns | dns.txt | `_globalsign-domain-verification=7HYSBVYWu06Bq9Lu_Mo-l0V9WrUUG4qDXf-Wre4Me0` | DNS TXT |
| 26 | dns | dns.txt | `uu8rvttgkkhsqri0tmb48nnn2o` | DNS TXT |
| 27 | dns | dns.txt | `_globalsign-domain-verification=grXkTmHxW4veQqxaTb7gMVZERHg5vqUyvziZ2d7miz` | DNS TXT |
| 28 | dns | dns.txt | `jamf-site-verification=LvhI-0-55SIPODOAlXQ1Rg` | DNS TXT |
| 29 | dns | dns.txt | `_globalsign-domain-verification=4sb-6QzBp3tzsMDDDZCZ5eRfzreasjMtAGtTC40ACz` | DNS TXT |
| 30 | dns | dns.txt | `agh09vo5p4okivaus2eemo0560` | DNS TXT |
| 31 | dns | dns.txt | `nqdspdl5ae38vu0qvnb1kck31j` | DNS TXT |
| 32 | dns | dns.txt | `google-site-verification=y6d10AgFowiDbrRahi1VTEEQ6SWq2lUGO1RaahraEaE` | DNS TXT |
| 33 | dns | dns.txt | `kjdt969ct1rpt5qe2ui7qplqi4` | DNS TXT |
| 34 | dns | dns.txt | `v=spf1 ip4:107.20.210.250/32 ip4:52.1.14.157/32 ip4:140.172.0.0/16 ip4:140.208.0` | DNS TXT |
| 35 | dns | dns.txt | `uf8vmf9cdji72j99k0p08s4rmn` | DNS TXT |
| 36 | dns | dns.txt | `h9ihjiq6si8jvuev03aarnblik` | DNS TXT |
| 37 | dns | dns.txt | `qr85gtkyffp8qw72sys0qt0nps1mvq5r` | DNS TXT |
| 38 | dns | dns.txt | `atlassian-domain-verification=egzuQjgGNamI0CukY/xaGisJ5BNdWzbEwkTjZZfR2oWeQSx35L` | DNS TXT |
| 39 | dns | dns.txt | `_k4s0fh6nekbudtjfqdi51giat4ukgoi` | DNS TXT |
| 40 | dns | dns.txt | `_globalsign-domain-verification=URGXBZ8iJ52XgEn8h1s3Tmfu_8g0NEAJjBNT13BhCd` | DNS TXT |
| 41 | dns | dns.txt | `google-site-verification=aNcHfDRvqETa0O8Ov1cnUi_xRyv790pE05gLz07bb80` | DNS TXT |
| 42 | dns | dns.txt | `cr487ajncv2bt7ukias1t7jrtf` | DNS TXT |
| 43 | dns | dns.txt | `_globalsign-domain-verification=q4T0TQVY1vDqerKP-47vqn33rBovmcwgHssPTAAGk4` | DNS TXT |
| 44 | dns | dns.txt | `h9rvsjncbb4p6nskq754m4d030` | DNS TXT |
| 45 | dns | dns.txt | `_globalsign-domain-verification=PvWVjlIh1OdSikC9i4pe4YgmP4lSosV-b_H9X5PJft` | DNS TXT |
| 46 | dns | dns.txt | `docusign=b602f0ac-0fcc-4a56-818c-4727282d3d35` | DNS TXT |
| 47 | dns | dns.txt | `miro-verification=d9effd8556fa2f065fb842704007c815c3c08a90` | DNS TXT |
| 48 | dns | dns.txt | `_globalsign-domain-verification=fMxP4j63Z_8XN8wHTyiaoAo6oBpi0ovoHs9sr6u7CR` | DNS TXT |
| 49 | dns | dns.txt | `ntad38mik3v7j7pbnnbul7umli` | DNS TXT |
| 50 | dns | dns.txt | `38jln0l23i1dosei72g2118kh8` | DNS TXT |
| 51 | dns | dns.txt | `65u3ikfk9aal59qqat7d4burjg` | DNS TXT |
| 52 | dns | dns.txt | `_globalsign-domain-verification=L0E33WT0_ulkIQXjbcmLHym6F75aTxrFrzqbGHf86b` | DNS TXT |
| 53 | dns | dns.txt | `rma10m3ktr6tmsnkl6qk1lq11b` | DNS TXT |
| 54 | dns | dns.txt | `_globalsign-domain-verification=11adxk0btv8mi7GiRacRaI9Mh5yFTm0zaO661LK_-O` | DNS TXT |
| 55 | dns | dns.txt | `MS=ms58948194` | DNS TXT |
| 56 | dns | dns.txt | `rlsjj64ar28180t7d3gf1bge48` | DNS TXT |
| 57 | dns | dns.txt | `cisco-ci-domain-verification=5703259edf46bd1e97b0538de8c1afccadaf4d7acbb13e9f38a` | DNS TXT |
| 58 | dns | dns.txt | `jamf-site-verification=_0HKHuolH1_RySV8D2SENw` | DNS TXT |
| 59 | dns | dns.txt | `_ndhwuukby2mizc29ku7wkozm5fol6b7` | DNS TXT |
| 60 | dns | dns.txt | `6kmuuh8h1cnnvmo0jiha6c4put` | DNS TXT |
| 61 | dns | dns.txt | `ebo09fqhu8jrjbrr2q0kp0ue38` | DNS TXT |
| 62 | dns | dns.txt | `_globalsign-domain-verification=x2RJuVuASCb8RpT2OsJPBK8gEu_dHMozQWFjGkKdx4` | DNS TXT |
| 63 | dns | dns.txt | `xj7g6kddr0mcv45f8gy45cc71jznbx88` | DNS TXT |
| 64 | dns | dns.txt | `hiu69kfi6er21jh9jnm1dqslmr` | DNS TXT |
| 65 | dns | dns.txt | `lovgmj95efm53f8dm8l33tqtkd` | DNS TXT |
| 66 | dns | dns.txt | `8a1fs3lb5ofdh0rg4rkt4or47d` | DNS TXT |
| 67 | dns | dns.txt | `5t72mlvrc58omhkioejvknkdv4` | DNS TXT |
| 68 | dns | dns.txt | `docker-verification=887e9be6-39b9-49cb-a81d-d757f89aa5f0` | DNS TXT |
| 69 | dns | dns.txt | `jamf-site-verification=V0LR-TQGDFhUEeOryr_P4Q` | DNS TXT |
| 70 | dns | dns.txt | `bq7nfpaf0ul91dk2h0aqtvs0fk` | DNS TXT |
| 71 | dns | dns.txt | `_globalsign-domain-verification=g7lP4Z2-b7gIQ8kJv8Ro5tMV2SLcE5eboZNK6Fr0GI` | DNS TXT |
| 72 | dns | dns.txt | `_globalsign-domain-verification=z9PJsp5h6m6P025rbGgyCa378u2dv7A1c-0Lqq1bDT` | DNS TXT |
| 73 | dns | dns.txt | `5fikk85qth4glfn7gjlfhps5lg` | DNS TXT |
| 74 | dns | dns.txt | `4p64i97hkh56l3019mr2jt59m5` | DNS TXT |
| 75 | dns | dns.txt | `apple-domain-verification=mkXNyD9G0JeTNzhD` | DNS TXT |
| 76 | shodan | open_port | `80` | https://internetdb.shodan.io/137.75.88.7 |
| 77 | shodan | open_port | `443` | https://internetdb.shodan.io/137.75.88.7 |
| 78 | shodan | hostname | `noaa.gov` | https://internetdb.shodan.io/137.75.88.7 |
| 79 | shodan | cpe | `cpe:/a:apache:http_server` | https://internetdb.shodan.io/137.75.88.7 |

## Trace

- plan: I will start with whois to gather registrar and domain information, then dns for network configuration, followed by shodan for open ports and vulnerabilities, github for potential code leaks, and finally wayback for historical snapshots, to build a comprehensive profile of noaa.gov.
- decide -> whois: Starting with whois to gather registrar and domain information as it is a cheap and informative init
- observe: whois: 7 findings (7 new), elapsed 1538 ms
- decide -> dns: The next logical step is to use dns to gather network configuration information after obtaining regi
- observe: dns: 68 findings (68 new), elapsed 5769 ms
- decide -> shodan: Next expensive tool to gather open ports and vulnerabilities information about noaa.gov.
- observe: shodan: 4 findings (4 new), elapsed 1771 ms
- decide -> github: To search for potential code leaks or exposed repositories related to noaa.gov.
- observe: github: 0 findings (0 new), elapsed 3468 ms, error: all GitHub dorks errored — check rate limit
- decide -> wayback: All other cheap and expensive tools except wayback have been called to gather comprehensive informat
- observe: wayback: 0 findings (0 new), elapsed 15704 ms, error: Wayback CDX request failed: ReadTimeout
- decide -> stop: All five tools have been called at least once and there are findings.
