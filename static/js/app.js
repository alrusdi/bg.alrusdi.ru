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
        choose_game: function (do_not_hide_choosen) {
            this.is_processing = true;
            if ( ! do_not_hide_choosen) {
                this.choosen_game = false;
            }
            var vue_app = this;
            axios.post('/choose-game/', {'is_real': this.is_real, 'is_digital': this.is_digital})
                .then(function (response) {
                    vue_app.choosen_game = response.data.game;
                    vue_app.is_processing = false;
                })
                .catch(function (error) {
                    vue_app.is_processing = false;
                });
        },

        register_play: function (force_game_id) {
            var vue_app = this;
            var game_id = force_game_id | vue_app.choosen_game.id;
            vue_app.is_processing = true;
            axios.post('/register-play/', {'game_id': game_id})
                .then(function (response) {
                    vue_app.message = "Ok! Игра «"+vue_app.choosen_game.title+"» записана.";
                    vue_app.choosen_game = false;
                    vue_app.is_processing = false;

                    if (force_game_id) {
                        var el = document.getElementById("game-count-"+game_id);
                        if (el) el.innerHTML = response.data.result;
                    }
                })
                .catch(function (error) {
                    vue_app.is_processing = false;
                });
        },

        reject_play: function () {
            var vue_app = this;
            axios.post('/reject-play/',  {'game_id': vue_app.choosen_game.id})
                .then(function (response) {
                    vue_app.message = "Ok! Игра «"+vue_app.choosen_game.title+"» отменена.";
                    vue_app.choosen_game = false;
                    vue_app.is_processing = false;
                })
                .catch(function (error) {
                    vue_app.is_processing = false;
                });
        }
    }
});