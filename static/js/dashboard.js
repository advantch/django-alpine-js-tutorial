let chartComponent;

const index = {
    name: "home", id: 1, key: "index",
}

const adminApps = {
    todo: {
        name: "Todo App", id: 2, key: "todo",
        icon: listIconUrl,
        description: "todo app"
    },
    chart: {
        name: "Chart App", id: 3, key: "chart",
        icon: chartIconUrl,
        description: "chart app"
    },
}

function dashboard() {
    return {
        views: adminApps,
        apps: adminApps,
        activeView: index,
        data: {
            chart: {
                chartData: [],
                isLoading:false
            },
            todo: {
                list:[],
                isLoading:false
            }
        },
        hasNavigated: true,
        loading: false,
        appList: ["todo", "charts"],
        
        init() {
            this.views = {index, ...adminApps}
            // check for key from url
            let key = new URLSearchParams(location.search).get("view")
            if (this.appList.includes(key)) {
            this.changeView(key)
            }
            // after dom content loaded
            // set view for index page and add listener
            this.$nextTick(() => {
            if(key===null || key !== null && !this.appList.includes(key)){
                this.updateHistoryState('index', true)
            }
            this.setPopStateEventListener()
            })
        },
        // handle navigation button to previous page
        setPopStateEventListener(){
            //https://developer.mozilla.org/en-US/docs/Web/API/Window/popstate_event
            window.onpopstate = () => setTimeout(()=> {
                if(!this.checkNavigationUpdated()){
                    console.log("nav incomplete")
                    let url= new URL(window.location)
                    let key = url.searchParams.get('view')
                    this.changeView(key)
                }
            }, 0);
            this.checkNavigationUpdated()
        },
        // check navigation updated 
        checkNavigationUpdated(){
            let url= new URL(window.location)
            return this.activeView.key === url.searchParams.get('view')
        },

        // logic after changing view
        async changeView(key) {
            this.loading = true
            // fetch relevant data for view and navigate to view
            try {
                this.activeView = this.views[key]
                this.updateHistoryState(key)
                await this.setupView(key)
            } catch (e) {
                console.log(`${e} Error loading view`)
            }

            this.loading = false
        },
        // update the history
        updateHistoryState(view, replace=false){
            try {
                console.info(`update view to ${view}`)
                const url = new URL(window.location);
                url.searchParams.set('view', view);
                replace ? window.history.replaceState({}, '', url) : window.history.pushState({}, '', url);
            }catch(e){
                console.log(`${e} Error updating history state`)
            }
        },

        // add any logic required before rendering a view, e.g. fetching data
        async setupView(key) {

            // update todos
            if (key === this.apps.todo.key) {
                this.data.todo.isLoading = true,
                fetch('api/dashboard/todos')
                this.data.todo.list = JSON.parse(document.getElementById('todos').textContent)
                this.data.todo.isLoading = false
            }

            // update chart view
            if (key === this.apps.chart.key) {
                // instead of an api call we use the data already rendered by django
                this.data.chart.chartData = JSON.parse(document.getElementById('chartData').textContent)
                chartComponent = echarts.init(document.getElementById('chartArea'));
                chartComponent.setOption(buildChartOptions(this.data.chart.chartData))
                setTimeout(chartComponent.resize(), 100)
            
            }
        }
    }
}

//resize chart on window reload
window.onresize = function() {
    chartComponent.resize();
};