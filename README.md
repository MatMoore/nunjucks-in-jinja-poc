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
- Relative file paths not understood by Jinja, but we can potentially override this
- Keys must be quoted
- Building with `installJinjaCompat` may help: https://mozilla.github.io/nunjucks/api.html#installjinjacompat
- http://jbmoelker.github.io/jinja-compat-tests/expressions/comparisons/ has some useful tests