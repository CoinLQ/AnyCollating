
var myChart = echarts.init(document.getElementById('charts'), 'wonderland');

myChart.showLoading();

$.get('/api/sutra/treemap/', function (diskData) {
    myChart.hideLoading();

    function colorMappingChange(value) {
        var levelOption = getLevelOption(value);
        chart.setOption({
            series: [{
                levels: levelOption
            }]
        });
    }

    var formatUtil = echarts.format;

    function getLevelOption() {
        return [
            {
                itemStyle: {
                    normal: {
                        borderWidth: 0,
                        gapWidth: 5
                    }
                }
            },
            {
                itemStyle: {
                    normal: {
                        gapWidth: 1
                    }
                }
            },
            {
                colorSaturation: [0.35, 0.5],
                itemStyle: {
                    normal: {
                        gapWidth: 1,
                        borderColorSaturation: 0.6
                    }
                }
            }
        ];
    }

    myChart.setOption(option = {

        title: {
            text: '校对经本领取',
            left: 'center'
        },

        tooltip: {
            formatter: function (info) {
                var value = info.value;
                var treePathInfo = info.treePathInfo;
                var treePath = [];

                for (var i = 1; i < treePathInfo.length; i++) {
                    treePath.push(treePathInfo[i].name);
                }

                return [
                    '<a href="/apps/tasks/verify_sutra/"+ info.data.sutra_id ><div class="tooltip-title">' + formatUtil.encodeHTML(treePath.join('/')) + '</div></a>',
                    '总卷数: ' + formatUtil.addCommas(info.data.reel) + ' 卷',
                ].join('');
            }
        },

        series: [
            {
                name:'开放校对经目',
                type:'treemap',
                visibleMin: 300,
                label: {
                    show: true,
                    formatter: '{b}'
                },
                itemStyle: {
                    normal: {
                        borderColor: '#fff'
                    }
                },
                levels: getLevelOption(),
                data: diskData
            }
        ]
    });
});

myChart.on('click', function (params) {
    console.log(params);
    window.open("/apps/tasks/verify_sutra/"+ params.data.sutra_id);
});
