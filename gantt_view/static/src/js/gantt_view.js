/** @odoo-module **/

import { browser } from "@web/core/browser/browser";
import { getActiveHotkey } from "@web/core/hotkeys/hotkey_service";
import { Pager } from "@web/core/pager/pager";
import { useService } from "@web/core/utils/hooks";
import { ComparisonMenu } from "../comparison_menu/comparison_menu";
import { FavoriteMenu } from "../favorite_menu/favorite_menu";
import { FilterMenu } from "../filter_menu/filter_menu";
import { GroupByMenu } from "../group_by_menu/group_by_menu";
import { SearchBar } from "../search_bar/search_bar";
import { Dropdown } from "@web/core/dropdown/dropdown";
import { Dialog } from "@web/core/dialog/dialog";

import {
    Component,
    useState,
    onMounted,
    useExternalListener,
    useRef,
    useEffect,
    useSubEnv,
} from "@odoo/owl";

