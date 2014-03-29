<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="keywords" content="karmaid, karmaid.org, karma, stuff, submit, vote" />
    <title>Karmaid: Karma for everything</title>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
    <script src="${request.static_url('karmaid:static/js/karmaid.js')}" type="text/javascript"></script>
    <link href="${request.static_url('karmaid:static/css/karmaid.css')}" type="text/css" rel="stylesheet" />
    <style>#forkongithub a{background:#000;color:#fff;text-decoration:none;font-family:arial, sans-serif;text-align:center;font-weight:bold;padding:2px 30px;font-size:1rem;line-height:2rem;position:relative;}#forkongithub a::before,#forkongithub a::after{content:"";width:100%;display:block;position:absolute;top:1px;left:0;height:1px;background:#fff;}#forkongithub a::after{bottom:1px;top:auto;}@media screen and (min-width:500px){#forkongithub{position:absolute;display:block;top:0;right:0;width:200px;overflow:hidden;height:200px;}#forkongithub a{width:200px;position:absolute;top:60px;right:-60px;transform:rotate(45deg);-webkit-transform:rotate(45deg);box-shadow:2px 2px 5px rgba(0,0,0,0.8);}}</style>
</head>
<body>
<span id="forkongithub"><a href="https://github.com/hirokiky/karmaid" target="_blank">Edit me on GitHub</a></span>
<input id="api-karma" type="hidden" value="${request.route_url('api_karma')}" />
<input id="api-ranking" type="hidden" value="${request.route_url('api_ranking')}" />
<input id="host" type="hidden" value="${host}" />
<div class="nav">
    <div class="container">
        <div class="brand"><a href="${request.route_url('top')}">Karmaid</a></div>
        <div class="nav-link"><a href="#ranking">ranking</a></div>
        <div class="nav-link"><a href="#buttongenerator">button</a></div>
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
