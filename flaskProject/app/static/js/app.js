(function($) {
    $(document).ready(function ($) {
       // console.log($('.val_abv'));
        var state = $('.val_abv');

        var state_text = $('text');
        var state_tspan = $('tspan');
        console.log(state_text)

        state.each(function (index) {
            console.log($(this)[0]);
            var color = $(this)[0].getAttribute('color').toLowerCase();
            color = color.split(' ').join('');

            var etats =  $(this)[0].getAttribute('etats')
            var amount =  $(this)[0].getAttribute('amount')
            var month =  $(this)[0].getAttribute('month')

            var id_map = $(this)[0].innerHTML;

            console.log($('#'+ id_map));
            // $('#'+ id_map)[0].classList.add('is-active');
            // $('#'+ id_map)[0].style.fill = color;
            if (color === 'rosewood' || color === 'barbiepink') {
                color = 'pink'
            } else if (color === 'peach' || color === 'camel') {
                color = 'orange'
            } else if (color === 'auburn' || color === 'carmine' || color === 'cerise' || color === 'rust') {
                color = 'saddlebrown'
            } else if (color === 'amethyst' || color === 'ultramarine') {
                color = 'green'
            } else if (color === 'mauve' || color === 'ruby') {
                color = 'violet'
            } else if (color === 'capri') {
                color = 'darkgrey'
            } else if (color === 'champagne') {
                color = 'gold'
            } else if (color === 'emerald') {
                color = 'greenyellow'
            }

            $('#'+ id_map)[0].style.setProperty("fill", color, "important");

            console.log(color);
            console.log(etats);

            state_text.each(function () {
                if (etats === $(this)[0].innerHTML) {
                    $(this)[0].insertAdjacentHTML('beforeend', '<tspan class="amount" style="display: block; float: left; fill: red; font-size: 16px;">' + amount + ' ' + '</tspan><br>')
                }
            })
            state_tspan.each(function () {
                if (etats === $(this)[0].innerHTML) {
                    $(this)[0].insertAdjacentHTML('afterend', '<tspan class="amount" style="display: block; float: left; fill: red; font-size: 16px;">' + amount + ' ' + '</tspan><br>')
                }
            })
        });

    });
})(jQuery);