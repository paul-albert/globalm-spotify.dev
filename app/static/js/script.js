(function () {

    // clear results
    $('ul.results').html('');

    // set filter for search
    $('.dropdown-menu li a').click(function (e) {
        e.preventDefault();
        $.post(
            '/set-filter',
            {
                filter: $(this).attr('data-value')
            },
            function (data) {
                console.log(data);
                console.log("'set-filter' was performed.");
            }
        );
    });

    // search
    $('a.search-icon').click(function (e) {
        e.preventDefault();
        text = $('.form-control').val();
        if (text.length > 0) {
            $('p.error').html('');
            $.post(
                '/search',
                {
                    query: text
                },
                function (data) {
                    console.log(data);
                    console.log("'search' was performed.");
                    var counterBlock = $('li.counter');
                    var resultsBlock = $('ul.results');
                    counterBlock.html('');
                    resultsBlock.html('');
                    counterBlock.append('Counter: ' + data.counter);
                    rows = '';
                    for (var i = 0, len = data.items.length; i < len; i++) {
                        if (data.items[i].hasOwnProperty('images')) {
                            if (data.items[i].images.length > 0) {
                                img =
                                    '<img class="thumb" src="' +
                                    data.items[i].images[0].url +
                                    '" height="64" width="64">';
                            } else {
                                img = '';
                            }
                        } else {
                            img = '';
                        }
                        rows += '<li>' + img + ' ' + data.items[i].name + '</li>';
                    }
                    resultsBlock.append(rows);
                }
            );
        }
    });

})();
