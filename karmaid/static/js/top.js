requeirejs.config({
    baseURL: 'js/lib',
    paths: {
        app: './app'
    }
});

requirejs(['app/karmaid.js']);
