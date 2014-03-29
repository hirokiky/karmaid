<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="keywords" content="karmaid, karmaid.org, karma, stuff, submit, vote" />
    <title>Karmaid: Karma for everything</title>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
    <script src="${request.static_url('karmaid:static/js/karmaid.js')}" type="text/javascript"></script>
    <link href="${request.static_url('karmaid:static/css/karmaid.css')}" type="text/css" rel="stylesheet" />
</head>
<body>
<input id="api-karma" type="hidden" value="${request.route_url('api_karma')}" />
<input id="api-ranking" type="hidden" value="${request.route_url('api_ranking')}" />
<input id="host" type="hidden" value="${host}" />
<div class="nav">
    <div class="container">
        <div class="brand"><a href="${request.route_url('top')}">Karmaid</a></div>
        <div class="karmawidget">
            <script>var karmaid_stuff='karmaid';</script>
            <script src="${host}/widget.js" type="text/javascript"></script>
        </div>
    </div>
</div>
<div class="hero">
    <div class="container">
        <div class="hero-text">
            <div class="karma">
                <span class="karma-value"><span class="value"></span><sub class="karma-suffix">karma</sub></span>
            </div>
            <span class="subheading">
                Karma for everything.<br />
                Vote your feeling without login.
            </span>
        </div>
        <div class="hero-input">
            <p><input class="stuff-input" type="text" value="karmaid" placeholder="Put the target stuff" /></p>
            <button class="action inc">++</button>
            <button class="action dec">--</button>
        </div>
    </div>
</div>
<div class="main">
    <a name="ranking"></a>
    <div class="ranking">
        <div class="container">
            <h1><span class="best-font">Best</span> / <span class="worst-font">Worst</span> Karma</h1>
            <p>The best and worst 10 karma for the totally.</p>
            <div class="ranks">
                <ul class="best">
                </ul>
                <ul class="worst">
                </ul>
            </div>
            <div class="clearboth"></div>
            <p><button class="ranking-refresh">refresh</button></p>
        </div>
    </div>
    <a name="buttongenerator"></a>
    <div class="buttongenerator">
        <div class="container">
            <div class="generator">
                <h1>Create your button</h1>
                <div class="generator-input">
                    karma for <input type="text" placeholder="everything" />
                </div>
                <div class="generator-result">
                    <h3>Copy the code</h3>
                    <p>Enjoy your button. If you like it, copy and paste the code below into your site.</p>
                    <div class="sample-widget">
                        <script>var karmaid_stuff='karmaid';</script>
                        <script src="${host}/widget.js" type="text/javascript"></script>
                    </div>
                    <textarea cols="30" rows="2"></textarea>
                </div>
            </div>
        </div>
    </div>
</div>
<footer>
    <div class="container">
        <p>by <a href="http://hirokiky.org/">Hiroki KIYOHARA</a></p>
        <p>Repository <a href="https://github.com/hirokiky/karmaid">karmaid</a></p>
    </div>
</footer>
</body>
</htmL>
