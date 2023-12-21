/** @odoo-module */

import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"
const { Component, useRef, onMounted ,useState } = owl

export class WorkReport extends Component {
    setup(){
        this.state = useState({
            data:{},
            period: 7,
            chart:[],
        })
        this.WorkReport = useRef("WorkReport"),
        this.orm = useService("orm")

        onMounted(async()=> {
            await this.FetchData();
        })
    }

    async onPeriodChange(){
        if (this.state.chart.length !=0) {
            this.state.chart.forEach((chart)=> {
                chart.destroy()
            })
            this.FetchData()
        }
    }

    async FetchData(){
        const date = this.state.period
        console.log(date)
        this.state.data = await this.orm.call("work.report", "get_datas", [date]);

        this.charts(this.WorkReport.el,'bar',this.state.data.data_x,'Work Report',this.state.data.data_y)
    }

    charts(canvas,type,labels,label,data){
        this.state.chart.push(new Chart(
            canvas,
            {
                type:type,
                data: {
                    labels: labels,
                    datasets: [
                        {
                        label: label,
                        data: data,
                        }
                    ]
                },
            }
        ))
    }

}
WorkReport.template = "WorkReport"
registry.category("actions").add('employee_work_report_tags', WorkReport)
