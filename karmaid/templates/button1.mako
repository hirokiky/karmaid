<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="keywords" content="karmaid, karmaid.org, karma, stuff, submit, vote" />
    <title>Karmaid buttons</title>
    <link type="text/css" rel="stylesheet"  href="${request.static_url('karmaid:static/css/button.css')}" />
    <script src="${request.static_url('karmaid:static/js/lib/jquery-2.1.0.min.js')}"></script>
    <script src="${request.static_url('karmaid:static/js/lib/knockout-3.1.0.min.js')}"></script>
    <script src="${request.static_url('karmaid:static/js/app/api.js')}"></script>
    <script src="${request.static_url('karmaid:static/js/app/utils.js')}"></script>
    <script src="${request.static_url('karmaid:static/js/button.js')}"></script>
</head>
<body class="button-body">
<input id="api-url" type="hidden" value="${request.route_url('api_karma')}" />
<div class="wrapper">
    <div class="button">
        <div class="body-wrapper">
            <div class="stuff">${stuff}</div>
            <div class="action inc" data-bind="click: incClick">++</div>
            <div class="action dec" data-bind="click: decClick">--</div>
        </div>
    </div>
    <div class="karma"><a href="${stuff_url}" target="_blank"><span class="karma-value" data-bind="text: karma"></span></a></div>
</div>
</body>
</html>
