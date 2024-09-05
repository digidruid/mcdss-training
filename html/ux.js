// usage example: <button onclick="hideday('day1')">Done</button>

function hideday(id) {
    $(id).fadeToggle();
}

function showdays() {
    $(".dayx").show();
}

function showslide(id) {
    $(".slidex").fade()
    $(id).show()
}

