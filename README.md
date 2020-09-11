# Zeitgeist Eis

Heroku does not offer locales by default. You need to install them via
`heroku buildpacks:set https://github.com/heroku/heroku-buildpack-locale.git -a
yourporject`

Make sure to add the python buildpack

`Settings -> Add buildpack -> heroku/python`
