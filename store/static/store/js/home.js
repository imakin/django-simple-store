
// model_products is in products_js
var img_type = ['pic','front'];
var img_size = ['small', 'big', 'thumb'];
//for faster searching by sku, copy reference in indexing by sku
model_products["by_sku"] = {};
//as model_products is [], loop (forEach) somehow only iterates numeric item, and skip by_sku
model_products.forEach(function(item){
    var sku = item.fields.sku;
    // frontend_config in frontend_config_js
    var prefix = frontend_config.product_image_url_prefix;
    item.fields['images'] = {};
    img_type.forEach(function(tipe){
        item.fields['images'][tipe] = {};
        img_size.forEach(function(size){
            var url = prefix+frontend_config["product_image_url_format_"+tipe+"_"+size];
            url = url.replace(/(\[SKU\])/g, sku);
            item.fields['images'][tipe][size] = url;
        })
    });

    //for faster searching by sku, copy reference in indexing by sku
    model_products["by_sku"][sku] = item;
});
ready(function(){
});

app_product_list = new Vue({
    el: '#product-list-container',
    data: {
        products: model_products,
        frontend_config: frontend_config
    },
    mounted: function() {
    },
    computed: {
    },
    methods: {
        productImageId: function(sku, type) {
            return "product-image-"+type+sku;
        },
        listExpand: function(event) {
            this.$el.classList.add('expand');
            event.target.scrollIntoView({ behavior: 'smooth', block: 'center' });
            
            var box = this.$el.querySelector('.box');
            setTimeout(function(){
                box.classList.remove('folded');
                box.classList.add('expanded');
            },100);
        },
        listGrid: function(event) {
            this.$el.classList.remove('expand');
            this.$el.querySelectorAll('.image-box.front').forEach(function(item){
                item.classList.remove('front');
                item.classList.add('pic');
            });
        },
        addToCart: function(event) {
            var sku = event.target.getAttribute('data-sku');

        },
        switchImage: function(event) {
            var sku = event.target.getAttribute('data-sku');
            if (sku==null) {
                //clicked inner element (i, span)
                sku = event.target.parentNode.getAttribute('data-sku');
            }
            var liitem = document.querySelector('#product-list li.product-list-item[data-sku="'+sku+'"]');
            var imgbox = liitem.querySelector('.image-box');
            console.log(imgbox)
            if (imgbox.classList.contains('front')) {
                imgbox.classList.add('pic');
                imgbox.classList.remove('front');
            }
            else {
                imgbox.classList.remove('pic');
                imgbox.classList.add('front');
            }
        },
        actionBoxFold: function(event) {
            var box = event.target.closest('.box');
            box.classList.toggle('folded');
        }
    }

});

if (!('IntersectionObserver' in window) ||
    !('IntersectionObserverEntry' in window) ||
    !('intersectionRatio' in window.IntersectionObserverEntry.prototype)) {
    // load polyfill now
}
else {
    document.querySelector('body').classList.add('intersection-observed');
}
let observerProduct = new IntersectionObserver(function(entries){
        entries.forEach(function(entry) {
            var el = entry.target;
            document.querySelectorAll('.action-bar .box.expanded').forEach(function(el){
                el.classList.remove('expanded');
                el.classList.add('folded');
            });

            var box = el.querySelector('.box');
            box.classList.remove('folded');
            box.classList.add('expanded');
        })
    }, {
        root: null,
        rootMargin: '0px',
        threshold: 1.0
    }
);
document.querySelectorAll('.product-list-item').forEach(function(el){
    observerProduct.observe(el);
})