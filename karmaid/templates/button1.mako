<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="keywords" content="karmaid, karmaid.org, karma, stuff, submit, vote" />
    <title></title>
    <link type="text/css" rel="stylesheet"  href="${request.static_url('karmaid:static/css/karmaid.css')}" />
    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
    <script src="${request.static_url('karmaid:static/js/button.js')}"></script>
</head>
<body class="button-body">
<input id="api-url" type="hidden" value="${request.route_url('api_karma')}" />
<div class="wrapper">
    <div class="button">
        <div class="body-wrapper">
            <div class="stuff">${stuff}</div>
            <div class="action inc">++</div>
            <div class="action dec">--</div>
        </div>
    </div>
    <div class="karma"><a href="${stuff_url}" target="_blank"><span class="karma-value">Error</span></a></div>
</div>
</body>
</html>
