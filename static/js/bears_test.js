"use strict";

function initMap() {
  const map = new google.maps.Map($('#map')[0], {
    center: {
      lat: 25,
      lng: 55
    },
    scrollwheel: false,
    zoom: 5,
    zoomControl: true,
    panControl: false,
    streetViewControl: false,
    styles: MAPSTYLES,  // mapStyles is defined in mapstyles.js
    mapTypeId: google.maps.MapTypeId.TERRAIN
  });

  // When a user clicks on a bear, an info window about that bear will appear.
  //
  // When they click on another bear, we want the previous info window to
  // disappear, so that only one window is open at a time.
  //
  // To do this, we'll define a single InfoWindow instance. All markers will
  // share this instance.
  const docInfo = new google.maps.InfoWindow();

  // Retrieving the information with AJAX.
  //
  // If you want to see what `/api/bears` returns, you should check `server.py`
  $.get('/api/docs', (docs) => {
    for (const doc of doctors) {
      // Define the content of the infoWindow
      const docInfoContent = (`
        <div class="window-content">
          <div class="bear-thumbnail">
            <img
              src="/static/img/doctor_female.png"
              alt="doctor"
            />
          </div>

          <ul class="bear-info">
            <li><b>Facility name: </b>${fac.f_name_english}</li>
            <li><b>Facility address: </b>${fac.address_line_one}</li>
            <li><b>Location: </b>${fac.lat}, ${fac.lng}</li>
          </ul>
        </div>
      `);

      const docMarker = new google.maps.Marker({
        position: {
          lat: fac.lat,
          lng: fac.lng
        },
        title: `Facility: ${fac.f_name_english}`,
        icon: {
          url: '/static/img/doctor.svg',
          scaledSize: new google.maps.Size(50, 50)
        },
        map: map,
      });

      docMarker.addListener('click', () => {
        docInfo.close();
        docInfo.setContent(bearInfoContent);
        docInfo.open(map, bearMarker);
      });
    }
  }).fail(() => {
    alert((`
      We were unable to retrieve data about docs :(

      Did you remember to create the bears database and seed it?
      (See model.py and seed.py for more info).
    `));
  });

  // Google Maps also provides a built-in control panel that allows users to
  // toggle different map styles.
  //
  // Here's how you do it:
  //
  // Create a new StyledMapType object, passing it the array of styles,
  // as well as the name of the map style.
  //
  // The name will be displayed in a button on the map-type control panel.
  //
  // const styledMap = new google.maps.StyledMapType(
  //  MAPSTYLES,
  //  { name: "Arctic Map" }
  // );
  //
  // You would then set 'styles' in Map() constructor's options to 'styledMap'.
  // For example:
  //
  // const map = new google.maps.Map(document.getElementById('bear-map', {
  //   center: mapCenter,
  //   // ... etc.
  //   styles: styledMap
  // });
  //
  // Finally, you must associate the styled map with the MapTypeId and
  // set it to display.
  //
  // map.mapTypes.set('map_style', styledMap);
  // map.setMapTypeId('map_style');
}

