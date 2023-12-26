/** @odoo-module **/

import { registry } from "@web/core/registry"
import { useService } from "@web/core/utils/hooks"
const { Component, useRef, onMounted ,useState } = owl

export class GanttView extends Component {
    setup(){
        this.state = useState({
        })
        onMounted(async()=> {
            await this.FetchTask();
        })
    }
    FetchTask(){
        console.log('hi')
    }


}