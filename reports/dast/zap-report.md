# ZAP Scanning Report

ZAP by [Checkmarx](https://checkmarx.com/).


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 0 |
| Medium | 3 |
| Low | 9 |
| Informational | 11 |




## Insights

| Level | Reason | Site | Description | Statistic |
| --- | --- | --- | --- | --- |
| Info | Informational | http://localhost:8000 | Percentage of responses with status code 2xx | 57 % |
| Info | Informational | http://localhost:8000 | Percentage of responses with status code 3xx | 27 % |
| Info | Informational | http://localhost:8000 | Percentage of responses with status code 4xx | 10 % |
| Info | Informational | http://localhost:8000 | Percentage of responses with status code 5xx | 5 % |
| Info | Informational | http://localhost:8000 | Percentage of endpoints with content type application/javascript | 3 % |
| Info | Informational | http://localhost:8000 | Percentage of endpoints with content type text/css | 3 % |
| Info | Informational | http://localhost:8000 | Percentage of endpoints with content type text/html | 92 % |
| Info | Informational | http://localhost:8000 | Percentage of endpoints with method GET | 86 % |
| Info | Informational | http://localhost:8000 | Percentage of endpoints with method POST | 13 % |
| Info | Informational | http://localhost:8000 | Count of total endpoints | 51    |
| Info | Informational | http://localhost:8000 | Percentage of slow responses | 5 % |
| Info | Informational | https://cdnjs.cloudflare.com | Percentage of endpoints with content type application/javascript | 100 % |
| Info | Informational | https://cdnjs.cloudflare.com | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://cdnjs.cloudflare.com | Count of total endpoints | 1    |
| Info | Informational | https://code.jquery.com | Percentage of endpoints with content type application/javascript | 100 % |
| Info | Informational | https://code.jquery.com | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://code.jquery.com | Count of total endpoints | 1    |
| Info | Informational | https://fonts.googleapis.com | Percentage of endpoints with content type text/css | 100 % |
| Info | Informational | https://fonts.googleapis.com | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://fonts.googleapis.com | Count of total endpoints | 2    |
| Info | Informational | https://fonts.gstatic.com | Percentage of endpoints with content type font/woff2 | 100 % |
| Info | Informational | https://fonts.gstatic.com | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://fonts.gstatic.com | Count of total endpoints | 4    |
| Info | Informational | https://stackpath.bootstrapcdn.com | Percentage of endpoints with content type application/javascript | 50 % |
| Info | Informational | https://stackpath.bootstrapcdn.com | Percentage of endpoints with content type text/css | 50 % |
| Info | Informational | https://stackpath.bootstrapcdn.com | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://stackpath.bootstrapcdn.com | Count of total endpoints | 2    |
| Info | Informational | https://use.fontawesome.com | Percentage of endpoints with content type application/javascript | 100 % |
| Info | Informational | https://use.fontawesome.com | Percentage of endpoints with method GET | 100 % |
| Info | Informational | https://use.fontawesome.com | Count of total endpoints | 2    |







## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| Absence of Anti-CSRF Tokens | Medium | 4 |
| Content Security Policy (CSP) Header Not Set | Medium | Systemic |
| Source Code Disclosure - Python | Medium | 1 |
| Application Error Disclosure | Low | 4 |
| Cookie No HttpOnly Flag | Low | Systemic |
| Cross-Origin-Embedder-Policy Header Missing or Invalid | Low | 5 |
| Cross-Origin-Resource-Policy Header Missing or Invalid | Low | Systemic |
| Full Path Disclosure | Low | 13 |
| Permissions Policy Header Not Set | Low | Systemic |
| Private IP Disclosure | Low | 4 |
| Server Leaks Version Information via "Server" HTTP Response Header Field | Low | Systemic |
| X-Content-Type-Options Header Missing | Low | 4 |
| Authentication Request Identified | Informational | 2 |
| Base64 Disclosure | Informational | 12 |
| Modern Web Application | Informational | Systemic |
| Non-Storable Content | Informational | Systemic |
| Sec-Fetch-Dest Header is Missing | Informational | 3 |
| Sec-Fetch-Mode Header is Missing | Informational | 3 |
| Sec-Fetch-Site Header is Missing | Informational | 3 |
| Sec-Fetch-User Header is Missing | Informational | 3 |
| Session Management Response Identified | Informational | 11 |
| Storable and Cacheable Content | Informational | 1 |
| User Controllable HTML Element Attribute (Potential XSS) | Informational | 8 |




## Alert Detail



### [ Absence of Anti-CSRF Tokens ](https://www.zaproxy.org/docs/alerts/10202/)



##### Medium (Low)

### Description

No Anti-CSRF tokens were found in a HTML submission form.
A cross-site request forgery is an attack that involves forcing a victim to send an HTTP request to a target destination without their knowledge or intent in order to perform an action as the victim. The underlying cause is application functionality using predictable URL/form actions in a repeatable way. The nature of the attack is that CSRF exploits the trust that a web site has for a user. By contrast, cross-site scripting (XSS) exploits the trust that a user has for a web site. Like XSS, CSRF attacks are not necessarily cross-site, but they can be. Cross-site request forgery is also known as CSRF, XSRF, one-click attack, session riding, confused deputy, and sea surf.

CSRF attacks are effective in a number of situations, including:
    * The victim has an active session on the target site.
    * The victim is authenticated via HTTP auth on the target site.
    * The victim is on the same local network as the target site.

CSRF has primarily been used to perform an action against a target site using the victim's privileges, but recent techniques have been discovered to disclose information by gaining access to the response. The risk of information disclosure is dramatically increased when the target site is vulnerable to XSS, because XSS can be used as a platform for CSRF, allowing the attack to operate within the bounds of the same-origin policy.

* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "language" "poster" "source" "title" ].`
* URL: http://localhost:8000/accounts/google/login/
  * Node Name: `http://localhost:8000/accounts/google/login/ ()(csrfmiddlewaretoken)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "language" "poster" "source" "title" ].`
* URL: http://localhost:8000/accounts/google/login/%3Fprocess=login
  * Node Name: `http://localhost:8000/accounts/google/login/ (process)(csrfmiddlewaretoken)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "language" "poster" "source" "title" ].`
* URL: http://localhost:8000/accounts/password/reset/
  * Node Name: `http://localhost:8000/accounts/password/reset/ ()(csrfmiddlewaretoken,email)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">`
  * Other Info: `No known Anti-CSRF token [anticsrf, CSRFToken, __RequestVerificationToken, csrfmiddlewaretoken, authenticity_token, OWASP_CSRFTOKEN, anoncsrf, csrf_token, _csrf, _csrfSecret, __csrf_magic, CSRF, _token, _csrf_token, _csrfToken] was found in the following HTML form: [Form 1: "language" "poster" "source" "title" ].`


Instances: 4

### Solution

Phase: Architecture and Design
Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid.
For example, use anti-CSRF packages such as the OWASP CSRFGuard.

Phase: Implementation
Ensure that your application is free of cross-site scripting issues, because most CSRF defenses can be bypassed using attacker-controlled script.

Phase: Architecture and Design
Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330).
Note that this can be bypassed using XSS.

Identify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation.
Note that this can be bypassed using XSS.

Use the ESAPI Session Management control.
This control includes a component for CSRF.

Do not use the GET method for any request that triggers a state change.

Phase: Implementation
Check the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
* [ https://cwe.mitre.org/data/definitions/352.html ](https://cwe.mitre.org/data/definitions/352.html)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 3

### [ Content Security Policy (CSP) Header Not Set ](https://www.zaproxy.org/docs/alerts/10038/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/auth
  * Node Name: `http://localhost:8000/auth`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/sitemap.xml
  * Node Name: `http://localhost:8000/sitemap.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
* [ https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://w3c.github.io/webappsec-csp/ ](https://w3c.github.io/webappsec-csp/)
* [ https://web.dev/articles/csp ](https://web.dev/articles/csp)
* [ https://caniuse.com/#feat=contentsecuritypolicy ](https://caniuse.com/#feat=contentsecuritypolicy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Source Code Disclosure - Python ](https://www.zaproxy.org/docs/alerts/10099/)



##### Medium (Medium)

### Description

Application Source Code was disclosed by the web server. - Python

* URL: http://localhost:8000/accounts/password/reset/
  * Node Name: `http://localhost:8000/accounts/password/reset/ ()(csrfmiddlewaretoken,email)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `        for dec in decorators:`
  * Other Info: ``


Instances: 1

### Solution

Ensure that application Source Code is not available with alternative extensions, and ensure that source code is not present within other files or data deployed to the web server, or served by the web server.

### Reference


* [ https://nhimg.org/twitter-breach ](https://nhimg.org/twitter-breach)


#### CWE Id: [ 540 ](https://cwe.mitre.org/data/definitions/540.html)


#### WASC Id: 13

#### Source ID: 3

### [ Application Error Disclosure ](https://www.zaproxy.org/docs/alerts/90022/)



##### Low (Medium)

### Description

This page contains an error/warning message that may disclose sensitive information like the location of the file that produced the unhandled exception. This information can be used to launch further attacks against the web application. The alert could be a false positive if the error message is found inside a documentation page.

* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 500 Internal Server Error`
  * Other Info: ``
* URL: http://localhost:8000/accounts/google/login/
  * Node Name: `http://localhost:8000/accounts/google/login/ ()(csrfmiddlewaretoken)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 500 Internal Server Error`
  * Other Info: ``
* URL: http://localhost:8000/accounts/google/login/%3Fprocess=login
  * Node Name: `http://localhost:8000/accounts/google/login/ (process)(csrfmiddlewaretoken)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 500 Internal Server Error`
  * Other Info: ``
* URL: http://localhost:8000/accounts/password/reset/
  * Node Name: `http://localhost:8000/accounts/password/reset/ ()(csrfmiddlewaretoken,email)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `HTTP/1.1 500 Internal Server Error`
  * Other Info: ``


Instances: 4

### Solution

Review the source code of this page. Implement custom error pages. Consider implementing a mechanism to provide a unique error reference/identifier to the client (browser) while logging the details on the server side and not exposing them to the user.

### Reference



#### CWE Id: [ 550 ](https://cwe.mitre.org/data/definitions/550.html)


#### WASC Id: 13

#### Source ID: 3

### [ Cookie No HttpOnly Flag ](https://www.zaproxy.org/docs/alerts/10010/)



##### Low (Medium)

### Description

A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript. If a malicious script can be run on this page then the cookie will be accessible and can be transmitted to another site. If this is a session cookie then session hijacking may be possible.

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `Set-Cookie: csrftoken`
  * Other Info: ``
* URL: http://localhost:8000/accounts/google/login/
  * Node Name: `http://localhost:8000/accounts/google/login/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `Set-Cookie: csrftoken`
  * Other Info: ``
* URL: http://localhost:8000/accounts/login/
  * Node Name: `http://localhost:8000/accounts/login/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `Set-Cookie: csrftoken`
  * Other Info: ``
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `Set-Cookie: csrftoken`
  * Other Info: ``
* URL: http://localhost:8000/register
  * Node Name: `http://localhost:8000/register`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `Set-Cookie: csrftoken`
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that the HttpOnly flag is set for all cookies.

### Reference


* [ https://owasp.org/www-community/HttpOnly ](https://owasp.org/www-community/HttpOnly)


#### CWE Id: [ 1004 ](https://cwe.mitre.org/data/definitions/1004.html)


#### WASC Id: 13

#### Source ID: 3

### [ Cross-Origin-Embedder-Policy Header Missing or Invalid ](https://www.zaproxy.org/docs/alerts/90004/)



##### Low (Medium)

### Description

Cross-Origin-Embedder-Policy header is a response header that prevents a document from loading any cross-origin resources that don't explicitly grant the document permission (using CORP or CORS).

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: `Cross-Origin-Embedder-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/accounts/google/login/
  * Node Name: `http://localhost:8000/accounts/google/login/`
  * Method: `GET`
  * Parameter: `Cross-Origin-Embedder-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/auth
  * Node Name: `http://localhost:8000/auth`
  * Method: `GET`
  * Parameter: `Cross-Origin-Embedder-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/`
  * Method: `GET`
  * Parameter: `Cross-Origin-Embedder-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/register
  * Node Name: `http://localhost:8000/register`
  * Method: `GET`
  * Parameter: `Cross-Origin-Embedder-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 5

### Solution

Ensure that the application/web server sets the Cross-Origin-Embedder-Policy header appropriately, and that it sets the Cross-Origin-Embedder-Policy header to 'require-corp' for documents.
If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Embedder-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-embedder-policy).

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 14

#### Source ID: 3

### [ Cross-Origin-Resource-Policy Header Missing or Invalid ](https://www.zaproxy.org/docs/alerts/90004/)



##### Low (Medium)

### Description

Cross-Origin-Resource-Policy header is an opt-in header designed to counter side-channels attacks like Spectre. Resource should be specifically set as shareable amongst different origins.

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/auth
  * Node Name: `http://localhost:8000/auth`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/static/Lab/ssrf.js
  * Node Name: `http://localhost:8000/static/Lab/ssrf.js`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/static/introduction/style4.css
  * Node Name: `http://localhost:8000/static/introduction/style4.css`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that the application/web server sets the Cross-Origin-Resource-Policy header appropriately, and that it sets the Cross-Origin-Resource-Policy header to 'same-origin' for all web pages.
'same-site' is considered as less secured and should be avoided.
If resources must be shared, set the header to 'cross-origin'.
If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Resource-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-resource-policy).

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 14

#### Source ID: 3

### [ Full Path Disclosure ](https://www.zaproxy.org/docs/alerts/110009/)



##### Low (Low)

### Description

The full path of files which might be sensitive has been exposed to the client.

* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``
* URL: http://localhost:8000/usr/local/lib/python3.10/site-packages/allauth/socialaccount/adapter.py,
  * Node Name: `http://localhost:8000/usr/local/lib/python3.10/site-packages/allauth/socialaccount/adapter.py,`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``
* URL: http://localhost:8000/usr/local/lib/python3.10/site-packages/allauth/socialaccount/models.py,
  * Node Name: `http://localhost:8000/usr/local/lib/python3.10/site-packages/allauth/socialaccount/models.py,`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``
* URL: http://localhost:8000/usr/local/lib/python3.10/site-packages/allauth/socialaccount/providers/base/mixins.py,
  * Node Name: `http://localhost:8000/usr/local/lib/python3.10/site-packages/allauth/socialaccount/providers/base/mixins.py,`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``
* URL: http://localhost:8000/usr/local/lib/python3.10/site-packages/allauth/socialaccount/providers/base/provider.py,
  * Node Name: `http://localhost:8000/usr/local/lib/python3.10/site-packages/allauth/socialaccount/providers/base/provider.py,`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``
* URL: http://localhost:8000/usr/local/lib/python3.10/site-packages/allauth/socialaccount/providers/oauth2/views.py,
  * Node Name: `http://localhost:8000/usr/local/lib/python3.10/site-packages/allauth/socialaccount/providers/oauth2/views.py,`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``
* URL: http://localhost:8000/usr/local/lib/python3.10/site-packages/django/core/handlers/base.py,
  * Node Name: `http://localhost:8000/usr/local/lib/python3.10/site-packages/django/core/handlers/base.py,`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``
* URL: http://localhost:8000/usr/local/lib/python3.10/site-packages/django/core/handlers/exception.py,
  * Node Name: `http://localhost:8000/usr/local/lib/python3.10/site-packages/django/core/handlers/exception.py,`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``
* URL: http://localhost:8000/usr/local/lib/python3.10/site-packages/django/db/models/manager.py,
  * Node Name: `http://localhost:8000/usr/local/lib/python3.10/site-packages/django/db/models/manager.py,`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``
* URL: http://localhost:8000/usr/local/lib/python3.10/site-packages/django/db/models/query.py,
  * Node Name: `http://localhost:8000/usr/local/lib/python3.10/site-packages/django/db/models/query.py,`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``
* URL: http://localhost:8000/accounts/google/login/
  * Node Name: `http://localhost:8000/accounts/google/login/ ()(csrfmiddlewaretoken)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``
* URL: http://localhost:8000/accounts/google/login/%3Fprocess=login
  * Node Name: `http://localhost:8000/accounts/google/login/ (process)(csrfmiddlewaretoken)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``
* URL: http://localhost:8000/accounts/password/reset/
  * Node Name: `http://localhost:8000/accounts/password/reset/ ()(csrfmiddlewaretoken,email)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `/usr/`
  * Other Info: ``


Instances: 13

### Solution

Disable directory browsing in your web server. Refer to the web server documentation.

### Reference


* [ https://owasp.org/www-community/attacks/Full_Path_Disclosure ](https://owasp.org/www-community/attacks/Full_Path_Disclosure)


#### CWE Id: [ 209 ](https://cwe.mitre.org/data/definitions/209.html)


#### WASC Id: 13

#### Source ID: 3

### [ Permissions Policy Header Not Set ](https://www.zaproxy.org/docs/alerts/10063/)



##### Low (Medium)

### Description

Permissions Policy Header is an added layer of security that helps to restrict from unauthorized access or usage of browser/client features by web resources. This policy ensures the user privacy by limiting or specifying the features of the browsers can be used by the web resources. Permissions Policy provides a set of standard HTTP headers that allow website owners to limit which features of browsers can be used by the page such as camera, microphone, location, full screen etc.

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/auth
  * Node Name: `http://localhost:8000/auth`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/sitemap.xml
  * Node Name: `http://localhost:8000/sitemap.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that your web server, application server, load balancer, etc. is configured to set the Permissions-Policy header.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy)
* [ https://developer.chrome.com/blog/feature-policy/ ](https://developer.chrome.com/blog/feature-policy/)
* [ https://scotthelme.co.uk/a-new-security-header-feature-policy/ ](https://scotthelme.co.uk/a-new-security-header-feature-policy/)
* [ https://w3c.github.io/webappsec-feature-policy/ ](https://w3c.github.io/webappsec-feature-policy/)
* [ https://www.smashingmagazine.com/2018/12/feature-policy/ ](https://www.smashingmagazine.com/2018/12/feature-policy/)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Private IP Disclosure ](https://www.zaproxy.org/docs/alerts/2/)



##### Low (Medium)

### Description

A private IP (such as 10.x.x.x, 172.x.x.x, 192.168.x.x) or an Amazon EC2 private hostname (for example, ip-10-0-56-78) has been found in the HTTP response body. This information might be helpful for further attacks targeting internal systems.

* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `172.18.0.1`
  * Other Info: `172.18.0.1
`
* URL: http://localhost:8000/accounts/google/login/
  * Node Name: `http://localhost:8000/accounts/google/login/ ()(csrfmiddlewaretoken)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `172.18.0.1`
  * Other Info: `172.18.0.1
`
* URL: http://localhost:8000/accounts/google/login/%3Fprocess=login
  * Node Name: `http://localhost:8000/accounts/google/login/ (process)(csrfmiddlewaretoken)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `172.18.0.1`
  * Other Info: `172.18.0.1
`
* URL: http://localhost:8000/accounts/password/reset/
  * Node Name: `http://localhost:8000/accounts/password/reset/ ()(csrfmiddlewaretoken,email)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `172.18.0.1`
  * Other Info: `172.18.0.1
`


Instances: 4

### Solution

Remove the private IP address from the HTTP response body. For comments, use JSP/ASP/PHP comment instead of HTML/JavaScript comment which can be seen by client browsers.

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc1918 ](https://datatracker.ietf.org/doc/html/rfc1918)


#### CWE Id: [ 497 ](https://cwe.mitre.org/data/definitions/497.html)


#### WASC Id: 13

#### Source ID: 3

### [ Server Leaks Version Information via "Server" HTTP Response Header Field ](https://www.zaproxy.org/docs/alerts/10036/)



##### Low (High)

### Description

The web/application server is leaking version information via the "Server" HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.10.4`
  * Other Info: ``
* URL: http://localhost:8000/ba
  * Node Name: `http://localhost:8000/ba`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.10.4`
  * Other Info: ``
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.10.4`
  * Other Info: ``
* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.10.4`
  * Other Info: ``
* URL: http://localhost:8000/sitemap.xml
  * Node Name: `http://localhost:8000/sitemap.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `WSGIServer/0.2 CPython/3.10.4`
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that your web server, application server, load balancer, etc. is configured to suppress the "Server" header or provide generic details.

### Reference


* [ https://httpd.apache.org/docs/current/mod/core.html#servertokens ](https://httpd.apache.org/docs/current/mod/core.html#servertokens)
* [ https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10) ](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10))
* [ https://www.troyhunt.com/shhh-dont-let-your-response-headers/ ](https://www.troyhunt.com/shhh-dont-let-your-response-headers/)


#### CWE Id: [ 497 ](https://cwe.mitre.org/data/definitions/497.html)


#### WASC Id: 13

#### Source ID: 3

### [ X-Content-Type-Options Header Missing ](https://www.zaproxy.org/docs/alerts/10021/)



##### Low (Medium)

### Description

The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.

* URL: http://localhost:8000/static/Lab/ssrf.css
  * Node Name: `http://localhost:8000/static/Lab/ssrf.css`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: http://localhost:8000/static/Lab/ssrf.js
  * Node Name: `http://localhost:8000/static/Lab/ssrf.js`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: http://localhost:8000/static/Lab/xss.js
  * Node Name: `http://localhost:8000/static/Lab/xss.js`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: http://localhost:8000/static/introduction/style4.css
  * Node Name: `http://localhost:8000/static/introduction/style4.css`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`


Instances: 4

### Solution

Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.
If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.

### Reference


* [ https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85) ](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85))
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Authentication Request Identified ](https://www.zaproxy.org/docs/alerts/10111/)



##### Informational (High)

### Description

The given request has been identified as an authentication request. The 'Other Info' field contains a set of key=value lines which identify any relevant fields. If the request is in a context which has an Authentication Method set to "Auto-Detect" then this rule will change the authentication to match the request identified.

* URL: http://localhost:8000/accounts/login/
  * Node Name: `http://localhost:8000/accounts/login/ ()(csrfmiddlewaretoken,login,password,remember)`
  * Method: `POST`
  * Parameter: `login`
  * Attack: ``
  * Evidence: `password`
  * Other Info: `userParam=login
userValue=ZAP
passwordParam=password
referer=http://localhost:8000/accounts/login/
csrfToken=csrfmiddlewaretoken`
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/ ()(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `username`
  * Attack: ``
  * Evidence: `password`
  * Other Info: `userParam=username
userValue=ZAP
passwordParam=password
referer=http://localhost:8000/login/
csrfToken=csrfmiddlewaretoken`


Instances: 2

### Solution

This is an informational alert rather than a vulnerability and so there is nothing to fix.

### Reference


* [ https://www.zaproxy.org/docs/desktop/addons/authentication-helper/auth-req-id/ ](https://www.zaproxy.org/docs/desktop/addons/authentication-helper/auth-req-id/)



#### Source ID: 3

### [ Base64 Disclosure ](https://www.zaproxy.org/docs/alerts/10094/)



##### Informational (Medium)

### Description

Base64 encoded data was disclosed by the application/web server. Note: in the interests of performance not all base64 strings in the response were analyzed individually, the entire response should be looked at by the analyst/security team/developer(s).

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `kjEMSDjT0RxmYbsfbh5r6MtVfrxCurkg6LVNuIbwERIxMHLy3WV67GckDqYXjh7r`
  * Other Info: `�1H8��fa�nk��U~�B�� �M���10r��ez�g$���`
* URL: http://localhost:8000/accounts/google/login/
  * Node Name: `http://localhost:8000/accounts/google/login/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `98qQDvDLHIS7wsCL6yFp8PiW9ph3A5GhNhdDmHztyUxsTWLjcpPwLJhERQJ1s0nM`
  * Other Info: `�ʐ��������!i�����w��6C�|��LlMb�r��,�DEu�I�`
* URL: http://localhost:8000/accounts/google/login/%3Fprocess=login
  * Node Name: `http://localhost:8000/accounts/google/login/ (process)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `98qQDvDLHIS7wsCL6yFp8PiW9ph3A5GhNhdDmHztyUxsTWLjcpPwLJhERQJ1s0nM`
  * Other Info: `�ʐ��������!i�����w��6C�|��LlMb�r��,�DEu�I�`
* URL: http://localhost:8000/accounts/login/
  * Node Name: `http://localhost:8000/accounts/login/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `98qQDvDLHIS7wsCL6yFp8PiW9ph3A5GhNhdDmHztyUxsTWLjcpPwLJhERQJ1s0nM`
  * Other Info: `�ʐ��������!i�����w��6C�|��LlMb�r��,�DEu�I�`
* URL: http://localhost:8000/accounts/password/reset/
  * Node Name: `http://localhost:8000/accounts/password/reset/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `98qQDvDLHIS7wsCL6yFp8PiW9ph3A5GhNhdDmHztyUxsTWLjcpPwLJhERQJ1s0nM`
  * Other Info: `�ʐ��������!i�����w��6C�|��LlMb�r��,�DEu�I�`
* URL: http://localhost:8000/accounts/signup/
  * Node Name: `http://localhost:8000/accounts/signup/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `98qQDvDLHIS7wsCL6yFp8PiW9ph3A5GhNhdDmHztyUxsTWLjcpPwLJhERQJ1s0nM`
  * Other Info: `�ʐ��������!i�����w��6C�|��LlMb�r��,�DEu�I�`
* URL: http://localhost:8000/auth
  * Node Name: `http://localhost:8000/auth`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4`
  * Other Info: `��󏽁T8u�p�d� 6g,E��(�Iai������7]"��+����s�%�`
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `98qQDvDLHIS7wsCL6yFp8PiW9ph3A5GhNhdDmHztyUxsTWLjcpPwLJhERQJ1s0nM`
  * Other Info: `�ʐ��������!i�����w��6C�|��LlMb�r��,�DEu�I�`
* URL: http://localhost:8000/register
  * Node Name: `http://localhost:8000/register`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `98qQDvDLHIS7wsCL6yFp8PiW9ph3A5GhNhdDmHztyUxsTWLjcpPwLJhERQJ1s0nM`
  * Other Info: `�ʐ��������!i�����w��6C�|��LlMb�r��,�DEu�I�`
* URL: http://localhost:8000/accounts/google/login/
  * Node Name: `http://localhost:8000/accounts/google/login/ ()(csrfmiddlewaretoken)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `kufNYaofG5jufySF1GYGMAyucsoWHxdDYD2AHmkXxhYPC21d7x8NpuxcUTQUzsU8`
  * Other Info: `���a���$��f0�r�C`=�i�m]���\Q4��<`
* URL: http://localhost:8000/accounts/google/login/%3Fprocess=login
  * Node Name: `http://localhost:8000/accounts/google/login/ (process)(csrfmiddlewaretoken)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `fm4iAOgpKr4tjaKtbgowCG4qrYVDQq0CTvR5j0c7BDJOGET1h7yDfA389pnBIlH7`
  * Other Info: `~n" �)*�-���n
0n*��CB�N�y�G;2ND����|����"Q�`
* URL: http://localhost:8000/accounts/signup/
  * Node Name: `http://localhost:8000/accounts/signup/ ()(csrfmiddlewaretoken,email,password1,password2,username)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `98qQDvDLHIS7wsCL6yFp8PiW9ph3A5GhNhdDmHztyUxsTWLjcpPwLJhERQJ1s0nM`
  * Other Info: `�ʐ��������!i�����w��6C�|��LlMb�r��,�DEu�I�`


Instances: 12

### Solution

Manually confirm that the Base64 data does not leak sensitive information, and that the data cannot be aggregated/used to exploit other vulnerabilities.

### Reference


* [ https://projects.webappsec.org/w/page/13246936/Information%20Leakage ](https://projects.webappsec.org/w/page/13246936/Information%20Leakage)


#### CWE Id: [ 319 ](https://cwe.mitre.org/data/definitions/319.html)


#### WASC Id: 13

#### Source ID: 3

### [ Modern Web Application ](https://www.zaproxy.org/docs/alerts/10109/)



##### Informational (Medium)

### Description

The application appears to be a modern web application. If you need to explore it automatically then the Client Spider may well be more effective than the standard one.

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" class="sidebar-list-items">Page 1</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`
* URL: http://localhost:8000/auth
  * Node Name: `http://localhost:8000/auth`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" class="sidebar-list-items">Page 1</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" class="sidebar-list-items">Page 1</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`
* URL: http://localhost:8000/register
  * Node Name: `http://localhost:8000/register`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" class="sidebar-list-items">Page 1</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`
* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `<a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a>`
  * Other Info: `Links have been found that do not have traditional href attributes, which is an indication that this is a modern web application.`

Instances: Systemic


### Solution

This is an informational alert and so no changes are required.

### Reference




#### Source ID: 3

### [ Non-Storable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are not storable by caching components such as proxy servers. If the response does not contain sensitive, personal or user-specific information, it may benefit from being stored and cached, to improve performance.

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `302`
  * Other Info: ``
* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `no-store`
  * Other Info: ``
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `no-store`
  * Other Info: ``
* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `500`
  * Other Info: ``
* URL: http://localhost:8000/sql
  * Node Name: `http://localhost:8000/sql`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `302`
  * Other Info: ``

Instances: Systemic


### Solution

The content may be marked as storable by ensuring that the following conditions are satisfied:
The request method must be understood by the cache and defined as being cacheable ("GET", "HEAD", and "POST" are currently defined as cacheable)
The response status code must be understood by the cache (one of the 1XX, 2XX, 3XX, 4XX, or 5XX response classes are generally understood)
The "no-store" cache directive must not appear in the request or response header fields
For caching by "shared" caches such as "proxy" caches, the "private" response directive must not appear in the response
For caching by "shared" caches such as "proxy" caches, the "Authorization" header field must not appear in the request, unless the response explicitly allows it (using one of the "must-revalidate", "public", or "s-maxage" Cache-Control response directives)
In addition to the conditions above, at least one of the following conditions must also be satisfied by the response:
It must contain an "Expires" header field
It must contain a "max-age" response directive
For "shared" caches such as "proxy" caches, it must contain a "s-maxage" response directive
It must contain a "Cache Control Extension" that allows it to be cached
It must have a status code that is defined as cacheable by default (200, 203, 204, 206, 300, 301, 404, 405, 410, 414, 501).

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc7234 ](https://datatracker.ietf.org/doc/html/rfc7234)
* [ https://datatracker.ietf.org/doc/html/rfc7231 ](https://datatracker.ietf.org/doc/html/rfc7231)
* [ https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html)


#### CWE Id: [ 524 ](https://cwe.mitre.org/data/definitions/524.html)


#### WASC Id: 13

#### Source ID: 3

### [ Sec-Fetch-Dest Header is Missing ](https://www.zaproxy.org/docs/alerts/90005/)



##### Informational (High)

### Description

Specifies how and where the data would be used. For instance, if the value is audio, then the requested resource must be audio data and not any other type of resource.

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: `Sec-Fetch-Dest`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: `Sec-Fetch-Dest`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/sitemap.xml
  * Node Name: `http://localhost:8000/sitemap.xml`
  * Method: `GET`
  * Parameter: `Sec-Fetch-Dest`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 3

### Solution

Ensure that Sec-Fetch-Dest header is included in request headers.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-Dest ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-Dest)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 3

### [ Sec-Fetch-Mode Header is Missing ](https://www.zaproxy.org/docs/alerts/90005/)



##### Informational (High)

### Description

Allows to differentiate between requests for navigating between HTML pages and requests for loading resources like images, audio etc.

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: `Sec-Fetch-Mode`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: `Sec-Fetch-Mode`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/sitemap.xml
  * Node Name: `http://localhost:8000/sitemap.xml`
  * Method: `GET`
  * Parameter: `Sec-Fetch-Mode`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 3

### Solution

Ensure that Sec-Fetch-Mode header is included in request headers.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-Mode ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-Mode)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 3

### [ Sec-Fetch-Site Header is Missing ](https://www.zaproxy.org/docs/alerts/90005/)



##### Informational (High)

### Description

Specifies the relationship between request initiator's origin and target's origin.

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: `Sec-Fetch-Site`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: `Sec-Fetch-Site`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/sitemap.xml
  * Node Name: `http://localhost:8000/sitemap.xml`
  * Method: `GET`
  * Parameter: `Sec-Fetch-Site`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 3

### Solution

Ensure that Sec-Fetch-Site header is included in request headers.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-Site ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-Site)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 3

### [ Sec-Fetch-User Header is Missing ](https://www.zaproxy.org/docs/alerts/90005/)



##### Informational (High)

### Description

Specifies if a navigation request was initiated by a user.

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: `Sec-Fetch-User`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/robots.txt
  * Node Name: `http://localhost:8000/robots.txt`
  * Method: `GET`
  * Parameter: `Sec-Fetch-User`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:8000/sitemap.xml
  * Node Name: `http://localhost:8000/sitemap.xml`
  * Method: `GET`
  * Parameter: `Sec-Fetch-User`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 3

### Solution

Ensure that Sec-Fetch-User header is included in user initiated requests.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-User ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-Fetch-User)


#### CWE Id: [ 352 ](https://cwe.mitre.org/data/definitions/352.html)


#### WASC Id: 9

#### Source ID: 3

### [ Session Management Response Identified ](https://www.zaproxy.org/docs/alerts/10112/)



##### Informational (Medium)

### Description

The given response has been identified as containing a session management token. The 'Other Info' field contains a set of header tokens that can be used in the Header Based Session Management Method. If the request is in a context which has a Session Management Method set to "Auto-Detect" then this rule will change the session management to use the tokens identified.

* URL: http://localhost:8000
  * Node Name: `http://localhost:8000`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://localhost:8000/accounts/google/login/
  * Node Name: `http://localhost:8000/accounts/google/login/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://localhost:8000/accounts/google/login/%3Fprocess=login
  * Node Name: `http://localhost:8000/accounts/google/login/ (process)`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://localhost:8000/accounts/login/
  * Node Name: `http://localhost:8000/accounts/login/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://localhost:8000/accounts/password/reset/
  * Node Name: `http://localhost:8000/accounts/password/reset/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://localhost:8000/accounts/signup/
  * Node Name: `http://localhost:8000/accounts/signup/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://localhost:8000/register
  * Node Name: `http://localhost:8000/register`
  * Method: `GET`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://localhost:8000/accounts/login/
  * Node Name: `http://localhost:8000/accounts/login/ ()(csrfmiddlewaretoken,login,password,remember)`
  * Method: `POST`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://localhost:8000/accounts/signup/
  * Node Name: `http://localhost:8000/accounts/signup/ ()(csrfmiddlewaretoken,email,password1,password2,username)`
  * Method: `POST`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/ ()(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `csrftoken`
  * Attack: ``
  * Evidence: `csrftoken`
  * Other Info: `cookie:csrftoken`


Instances: 11

### Solution

This is an informational alert rather than a vulnerability and so there is nothing to fix.

### Reference


* [ https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id/ ](https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id/)



#### Source ID: 3

### [ Storable and Cacheable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are storable by caching components such as proxy servers, and may be retrieved directly from the cache, rather than from the origin server by the caching servers, in response to similar requests from other users. If the response data is sensitive, personal or user-specific, this may result in sensitive information being leaked. In some cases, this may even result in a user gaining complete control of the session of another user, depending on the configuration of the caching components in use in their environment. This is primarily an issue where "shared" caching servers such as "proxy" caches are configured on the local network. This configuration is typically found in corporate or educational environments, for instance.

* URL: http://localhost:8000/sitemap.xml
  * Node Name: `http://localhost:8000/sitemap.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`


Instances: 1

### Solution

Validate that the response does not contain sensitive, personal or user-specific information. If it does, consider the use of the following HTTP response headers, to limit, or prevent the content being stored and retrieved from the cache by another user:
Cache-Control: no-cache, no-store, must-revalidate, private
Pragma: no-cache
Expires: 0
This configuration directs both HTTP 1.0 and HTTP 1.1 compliant caching servers to not store the response, and to not retrieve the response (without validation) from the cache, in response to a similar request.

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc7234 ](https://datatracker.ietf.org/doc/html/rfc7234)
* [ https://datatracker.ietf.org/doc/html/rfc7231 ](https://datatracker.ietf.org/doc/html/rfc7231)
* [ https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html)


#### CWE Id: [ 524 ](https://cwe.mitre.org/data/definitions/524.html)


#### WASC Id: 13

#### Source ID: 3

### [ User Controllable HTML Element Attribute (Potential XSS) ](https://www.zaproxy.org/docs/alerts/10031/)



##### Informational (Low)

### Description

This check looks at user-supplied input in query string parameters and POST data to identify where certain HTML attribute values might be controlled. This provides hot-spot detection for XSS (cross-site scripting) that will require further review by a security analyst to determine exploitability.

* URL: http://localhost:8000/accounts/login/
  * Node Name: `http://localhost:8000/accounts/login/ ()(csrfmiddlewaretoken,login,password,remember)`
  * Method: `POST`
  * Parameter: `login`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

http://localhost:8000/accounts/login/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
login=ZAP

The user-controlled value was:
zap`
* URL: http://localhost:8000/accounts/login/
  * Node Name: `http://localhost:8000/accounts/login/ ()(csrfmiddlewaretoken,login,password,remember)`
  * Method: `POST`
  * Parameter: `password`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

http://localhost:8000/accounts/login/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
password=ZAP

The user-controlled value was:
zap`
* URL: http://localhost:8000/accounts/signup/
  * Node Name: `http://localhost:8000/accounts/signup/ ()(csrfmiddlewaretoken,email,password1,password2,username)`
  * Method: `POST`
  * Parameter: `email`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

http://localhost:8000/accounts/signup/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
email=zaproxy@example.com

The user-controlled value was:
zaproxy@example.com`
* URL: http://localhost:8000/accounts/signup/
  * Node Name: `http://localhost:8000/accounts/signup/ ()(csrfmiddlewaretoken,email,password1,password2,username)`
  * Method: `POST`
  * Parameter: `password1`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

http://localhost:8000/accounts/signup/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
password1=ZAP

The user-controlled value was:
zap`
* URL: http://localhost:8000/accounts/signup/
  * Node Name: `http://localhost:8000/accounts/signup/ ()(csrfmiddlewaretoken,email,password1,password2,username)`
  * Method: `POST`
  * Parameter: `password2`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

http://localhost:8000/accounts/signup/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
password2=ZAP

The user-controlled value was:
zap`
* URL: http://localhost:8000/accounts/signup/
  * Node Name: `http://localhost:8000/accounts/signup/ ()(csrfmiddlewaretoken,email,password1,password2,username)`
  * Method: `POST`
  * Parameter: `username`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

http://localhost:8000/accounts/signup/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
username=ZAP

The user-controlled value was:
zap`
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/ ()(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `password`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

http://localhost:8000/login/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
password=ZAP

The user-controlled value was:
zap`
* URL: http://localhost:8000/login/
  * Node Name: `http://localhost:8000/login/ ()(csrfmiddlewaretoken,password,username)`
  * Method: `POST`
  * Parameter: `username`
  * Attack: ``
  * Evidence: ``
  * Other Info: `User-controlled HTML attribute values were found. Try injecting special characters to see if XSS might be possible. The page at the following URL:

http://localhost:8000/login/

appears to include user input in:
a(n) [input] tag [value] attribute

The user input found was:
username=ZAP

The user-controlled value was:
zap`


Instances: 8

### Solution

Validate all input and sanitize output it before writing to any HTML attributes.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)


#### CWE Id: [ 20 ](https://cwe.mitre.org/data/definitions/20.html)


#### WASC Id: 20

#### Source ID: 3


