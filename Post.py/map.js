
    //初始化地图对象，加载地图
    var map = new AMap.Map("container", {
        resizeEnable: true,
        zoom: 13
    });
    var m1 = new AMap.Marker({
        map: map,
        draggable:true,
        position: new AMap.LngLat(116.368904, 39.923423)
    });
    var m2 = new AMap.Marker({
        map: map,
        draggable:true,
        position:new AMap.LngLat(116.387271, 39.922501)
    });
    map.setFitView();
    
    var line,text;
    function computeDis(){
        var p1 = m1.getPosition();
        var p2 = m2.getPosition();
        var textPos = p1.divideBy(2).add(p2.divideBy(2));
        var distance = Math.round(p1.distance(p2));
        var path = [p1,p2];
        if(!line){
            line = new AMap.Polyline({
           		map:map,
              	strokeColor:'#80d8ff',
              	isOutline:true,
              	outlineColor:'white',
                path:path
            });
        }else{
            line.setPath(path);
        }
        if(!text){
            text = new AMap.Text({
              	text:'两点相距'+distance+'米',
                position: textPos,
                map:map,
              	style:{'background-color':'#29b6f6',
        				'border-color':'#e1f5fe',
        				'font-size':'12px'}
            })
        }else{
            text.setText('两点相距'+distance+'米')
            text.setPosition(textPos)
        }
    }
    computeDis();
    m1.on('dragging', computeDis)
    m2.on('dragging', computeDis)
