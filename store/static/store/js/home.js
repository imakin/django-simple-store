Vue.component('product-image-front', {
    props: ['sku'],
    template: '<div class="product-image-front">'+
            '<span class="model url url-small">'+
                frontend_config.product_image_url_prefix +
                frontend_config.product_image_url_format_front_small+
            '</span>'+
            '<span class="model url url-big">'+
                frontend_config.product_image_url_prefix +
                frontend_config.product_image_url_format_front_big+
            '</span>'+
            '</div>',
});
Vue.component('product-image-pic', {
    props: ['sku'],
    template: '<div class="product-image-pic">'+
            '<span class="model url url-small">'+
                frontend_config.product_image_url_prefix +
                frontend_config.product_image_url_format_pic_small+
            '</span>'+
            '<span class="model url url-big">'+
                frontend_config.product_image_url_prefix +
                frontend_config.product_image_url_format_pic_big+
            '</span>'+
            '</div>',
});


app_product_list = new Vue({
    el: '#product-list',
    data: {
        products: model_products,
        frontend_config: frontend_config
    },
    mounted: function() {
        this.$el.querySelectorAll(".product-image-pic").forEach(
            function(elem) {
                var img_small = elem.querySelector('.url-small');
                var img_big = elem.querySelector('.url-big');
                var img = document.createElement('img');
                img.src = img_small.textContent;
                img.setAttribute('data-img-big', img_big.textContent);
                elem.appendChild(img);
            }
        )
    }

})