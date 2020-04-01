// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides an SSM Maintenance Window resource
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const production = new aws.ssm.MaintenanceWindow("production", {
 *     cutoff: 1,
 *     duration: 3,
 *     schedule: "cron(0 16 ? * TUE *)",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_maintenance_window.html.markdown.
 */
export class MaintenanceWindow extends pulumi.CustomResource {
    /**
     * Get an existing MaintenanceWindow resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MaintenanceWindowState, opts?: pulumi.CustomResourceOptions): MaintenanceWindow {
        return new MaintenanceWindow(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:ssm/maintenanceWindow:MaintenanceWindow';

    /**
     * Returns true if the given object is an instance of MaintenanceWindow.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MaintenanceWindow {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MaintenanceWindow.__pulumiType;
    }

    /**
     * Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.
     */
    public readonly allowUnassociatedTargets!: pulumi.Output<boolean | undefined>;
    /**
     * The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.
     */
    public readonly cutoff!: pulumi.Output<number>;
    /**
     * A description for the maintenance window.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The duration of the Maintenance Window in hours.
     */
    public readonly duration!: pulumi.Output<number>;
    /**
     * Whether the maintenance window is enabled. Default: `true`.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * Timestamp in [ISO-8601 extended format](https://www.iso.org/iso-8601-date-and-time-format.html) when to no longer run the maintenance window.
     */
    public readonly endDate!: pulumi.Output<string | undefined>;
    /**
     * The name of the maintenance window.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The schedule of the Maintenance Window in the form of a [cron](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html) or rate expression.
     */
    public readonly schedule!: pulumi.Output<string>;
    /**
     * Timezone for schedule in [Internet Assigned Numbers Authority (IANA) Time Zone Database format](https://www.iana.org/time-zones). For example: `America/Los_Angeles`, `etc/UTC`, or `Asia/Seoul`.
     */
    public readonly scheduleTimezone!: pulumi.Output<string | undefined>;
    /**
     * Timestamp in [ISO-8601 extended format](https://www.iso.org/iso-8601-date-and-time-format.html) when to begin the maintenance window.
     */
    public readonly startDate!: pulumi.Output<string | undefined>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a MaintenanceWindow resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MaintenanceWindowArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MaintenanceWindowArgs | MaintenanceWindowState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as MaintenanceWindowState | undefined;
            inputs["allowUnassociatedTargets"] = state ? state.allowUnassociatedTargets : undefined;
            inputs["cutoff"] = state ? state.cutoff : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["duration"] = state ? state.duration : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["endDate"] = state ? state.endDate : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["schedule"] = state ? state.schedule : undefined;
            inputs["scheduleTimezone"] = state ? state.scheduleTimezone : undefined;
            inputs["startDate"] = state ? state.startDate : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as MaintenanceWindowArgs | undefined;
            if (!args || args.cutoff === undefined) {
                throw new Error("Missing required property 'cutoff'");
            }
            if (!args || args.duration === undefined) {
                throw new Error("Missing required property 'duration'");
            }
            if (!args || args.schedule === undefined) {
                throw new Error("Missing required property 'schedule'");
            }
            inputs["allowUnassociatedTargets"] = args ? args.allowUnassociatedTargets : undefined;
            inputs["cutoff"] = args ? args.cutoff : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["duration"] = args ? args.duration : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["endDate"] = args ? args.endDate : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["schedule"] = args ? args.schedule : undefined;
            inputs["scheduleTimezone"] = args ? args.scheduleTimezone : undefined;
            inputs["startDate"] = args ? args.startDate : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(MaintenanceWindow.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MaintenanceWindow resources.
 */
export interface MaintenanceWindowState {
    /**
     * Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.
     */
    readonly allowUnassociatedTargets?: pulumi.Input<boolean>;
    /**
     * The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.
     */
    readonly cutoff?: pulumi.Input<number>;
    /**
     * A description for the maintenance window.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The duration of the Maintenance Window in hours.
     */
    readonly duration?: pulumi.Input<number>;
    /**
     * Whether the maintenance window is enabled. Default: `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * Timestamp in [ISO-8601 extended format](https://www.iso.org/iso-8601-date-and-time-format.html) when to no longer run the maintenance window.
     */
    readonly endDate?: pulumi.Input<string>;
    /**
     * The name of the maintenance window.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The schedule of the Maintenance Window in the form of a [cron](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html) or rate expression.
     */
    readonly schedule?: pulumi.Input<string>;
    /**
     * Timezone for schedule in [Internet Assigned Numbers Authority (IANA) Time Zone Database format](https://www.iana.org/time-zones). For example: `America/Los_Angeles`, `etc/UTC`, or `Asia/Seoul`.
     */
    readonly scheduleTimezone?: pulumi.Input<string>;
    /**
     * Timestamp in [ISO-8601 extended format](https://www.iso.org/iso-8601-date-and-time-format.html) when to begin the maintenance window.
     */
    readonly startDate?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a MaintenanceWindow resource.
 */
export interface MaintenanceWindowArgs {
    /**
     * Whether targets must be registered with the Maintenance Window before tasks can be defined for those targets.
     */
    readonly allowUnassociatedTargets?: pulumi.Input<boolean>;
    /**
     * The number of hours before the end of the Maintenance Window that Systems Manager stops scheduling new tasks for execution.
     */
    readonly cutoff: pulumi.Input<number>;
    /**
     * A description for the maintenance window.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The duration of the Maintenance Window in hours.
     */
    readonly duration: pulumi.Input<number>;
    /**
     * Whether the maintenance window is enabled. Default: `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * Timestamp in [ISO-8601 extended format](https://www.iso.org/iso-8601-date-and-time-format.html) when to no longer run the maintenance window.
     */
    readonly endDate?: pulumi.Input<string>;
    /**
     * The name of the maintenance window.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The schedule of the Maintenance Window in the form of a [cron](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-cron.html) or rate expression.
     */
    readonly schedule: pulumi.Input<string>;
    /**
     * Timezone for schedule in [Internet Assigned Numbers Authority (IANA) Time Zone Database format](https://www.iana.org/time-zones). For example: `America/Los_Angeles`, `etc/UTC`, or `Asia/Seoul`.
     */
    readonly scheduleTimezone?: pulumi.Input<string>;
    /**
     * Timestamp in [ISO-8601 extended format](https://www.iso.org/iso-8601-date-and-time-format.html) when to begin the maintenance window.
     */
    readonly startDate?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
