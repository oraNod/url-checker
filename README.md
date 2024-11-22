# Ansible docsite redirect testing (WIP)

This repository contains a Python script and multiple `*.txt` files that contain url paths for Ansible community documentation.
The Python script uses the `.txt` files to construct urls and then generate a report that contains the HTTP status code of each url and, in the case of a redirect, the page to which the url is redirected.

## Redirects

Redirect rules are defined in the following `.htaccess` configuration files:

- [ansible/2.3](https://github.com/ansible/docsite/blob/main/ansible/2.3/.htaccess)
- [ansible/2.4](https://github.com/ansible/docsite/blob/main/ansible/2.4/.htaccess)
- [ansible/2.5](https://github.com/ansible/docsite/blob/main/ansible/2.5/.htaccess)
- [ansible/2.6](https://github.com/ansible/docsite/blob/main/ansible/2.6/.htaccess)
- [ansible/2.9](https://github.com/ansible/docsite/blob/main/ansible/2.6/.htaccess)
- [ansible/9](https://github.com/ansible/docsite/blob/main/ansible/9/.htaccess)
- [ansible/11](https://github.com/ansible/docsite/blob/main/ansible/11/.htaccess)

There are also redirect rules defined in a main [.htaccess](https://github.com/ansible/docsite/blob/main/.htaccess) configuration file that apply to the `devel` and `latest` versions.
Along with those rules, there are some redirects for versionless pages such as the `/ansible/playbooks_vault.html`.

Each of the redirect rules is similar to the following:

```bash
RedirectMatch "^(/ansible/[^/]+)/plugins/become/doas.html" "$1/collections/community/general/doas_become.html"
```

This rule matches urls that start with `/ansible/` followed by any characters except `/` and then matches the `/plugins/become/doas.html` path. The `$1` back reference then captures the first part, which is a version like `/ansible/2.4`. The url then redirects to the `/collections/community/general/doas_become.html` path.

For example, `/ansible/2.4/plugins/become/doas.html` would redirect to `/ansible/2.4/collections/community/general/doas_become.html`.

To test these redirects, the `.txt` files in the `redirects` folder contain the original paths and versions from the corresponding `.htaccess` configuration files in the `ansible/docsite` repository.

For example, the `redirects/ansible_2.4_redirects.txt` file contains this path: `/ansible/2.4/playbooks_roles.html`. This is the path in an Ansible 2.4 url that should be redirected to some other page. When you generate a url report, it contains the following:

```txt
URL: https://docs.ansible.com/ansible/2.4/playbooks_roles.html
Status: 302
Redirects to: http://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse.html
```

The `URL:` field shows the url that the script constructed from the path in the `redirects/ansible_2.4_redirects.txt` file. This is the url for which a redirect rule is in place.

The `Status:` field shows the HTTP status code that the url returns when you request that particular page. If a redirect rule is in place the code should be `301` for a permanent redirect or `302`.

Finally `Redirects to:` shows the url to which the page is redirected.

## Pages

Coming soon.
