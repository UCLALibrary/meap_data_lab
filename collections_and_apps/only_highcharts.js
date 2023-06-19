function chart() {
    console.log('a');
    chart = new Highcharts.Chart({
        chart: {
            type: 'pie',
            renderTo: 'container'
        },
        title: {
            text: 'Applications by Geography'
        },
    
        subtitle: {
            text: 'Click the slices to view sub-geographies.'
        },
    
        data: {
            csvURL: 'all_apps.csv',
        }
    });
}