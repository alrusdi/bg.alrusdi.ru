var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        is_processing: false,

        is_digital: true,
        is_real: true,

        choosen_game: false,
        choosen_game_id: false,

        message: ""
    },
    methods: {
        choose_game: function () {
            this.is_processing = true;
            this.choosen_game = false;
            var vue_app = this;
            axios.post('/choose-game/', {'is_real': this.is_real, 'is_digital': this.is_digital})
                .then(function (response) {
                    vue_app.choosen_game = response.data.game;
                    console.log(vue_app.choosen_game);
                    vue_app.is_processing = false;
                })
                .catch(function (error) {
                    vue_app.is_processing = false;
                });
        },

        register_play: function () {
            var vue_app = this;
            axios.post('/register-play/', {'game_id': vue_app.choosen_game.id})
                .then(function (response) {
                    vue_app.message = "Ok! Игра «%s» записана." % choosen_game.title;
                    vue_app.choosen_game = false;
                    vue_app.is_processing = false;
                })
                .catch(function (error) {
                    vue_app.is_processing = false;
                });
        },

        reject_play: function () {
            var vue_app = this;
            axios.post('/reject-play/',  {'game_id': vue_app.choosen_game.id})
                .then(function (response) {
                    vue_app.choosen_game = false;
                    vue_app.message = "Ok! Игра записана.";
                    vue_app.is_processing = false;
                })
                .catch(function (error) {
                    vue_app.is_processing = false;
                });
        }
    }
});