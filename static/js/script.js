ymaps.ready(init);
function init() {
    if (document.getElementById('coords').value === ''){
        var coords = [55.99706, 92.8764193]
    } else {
        var coords = document.getElementById('coords').value.split(',')
        var coords = coords.map(Number)
    }
    document.getElementById('coords').value = coords
    var myPlacemark,
        myMap = new ymaps.Map('map', {
            center: coords,
            zoom: 12
        }, {
            searchControlProvider: 'yandex#search'
        });
    myPlacemark = createPlacemark(coords);
    myMap.geoObjects.add(myPlacemark);

    // Слушаем клик на карте.
    myMap.events.add('click', function (e) {
        var coords = e.get('coords');

        // Если метка уже создана – просто передвигаем ее.
        if (myPlacemark) {
            myPlacemark.geometry.setCoordinates(coords);
        }
        // Если нет – создаем.
        else {
            myPlacemark = createPlacemark(coords);
            myMap.geoObjects.add(myPlacemark);
            // Слушаем событие окончания перетаскивания на метке.
            myPlacemark.events.add('dragend', function () {
                getAddress(myPlacemark.geometry.getCoordinates());
            });
        }
        document.getElementById('coords').value = coords
    });

    // Создание метки.
    function createPlacemark(coords) {
        return new ymaps.Placemark(coords, {}, {
            preset: 'islands#violetDotIconWithCaption',
            draggable: false
        });
    }
}