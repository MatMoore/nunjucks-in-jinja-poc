# Proof of concept - importing Nunjucks templates in Jinja

A quick PoC to flush out compatability issues between Nunjucks and Jinja.

## How to run
```
pip install flask # or `uv install`
```

```
flask --app main run
```


## Findings
- Use of === and !==
    - we cannot swap for loose equality without changing the meaning
    - == is inconsistent too: JS-style loose equality in nunjucks but python-style in Jinja https://github.com/mozilla/nunjucks/issues/750
    - Discussion from when === was added https://github.com/mozilla/nunjucks/pull/746
    - Example use: `{% if options.optional === true and options.value === true %}`
    - Not sure how to workaround this without obfuscating the expression
- Relative file paths not understood by Jinja, but we can potentially override this
- Keys must be quoted
- Building with `installJinjaCompat` may help: https://mozilla.github.io/nunjucks/api.html#installjinjacompat
- http://jbmoelker.github.io/jinja-compat-tests/expressions/comparisons/ has some useful tests