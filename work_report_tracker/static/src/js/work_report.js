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
    }



}
WorkReport.template = "WorkReport"
registry.category("actions").add('employee_work_report_tags', WorkReport)
