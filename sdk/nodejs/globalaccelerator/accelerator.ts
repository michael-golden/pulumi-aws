// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Creates a Global Accelerator accelerator.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.globalaccelerator.Accelerator("example", {
 *     attributes: {
 *         flowLogsEnabled: true,
 *         flowLogsS3Bucket: "example-bucket",
 *         flowLogsS3Prefix: "flow-logs/",
 *     },
 *     enabled: true,
 *     ipAddressType: "IPV4",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/globalaccelerator_accelerator.markdown.
 */
export class Accelerator extends pulumi.CustomResource {
    /**
     * Get an existing Accelerator resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AcceleratorState, opts?: pulumi.CustomResourceOptions): Accelerator {
        return new Accelerator(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:globalaccelerator/accelerator:Accelerator';

    /**
     * Returns true if the given object is an instance of Accelerator.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Accelerator {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Accelerator.__pulumiType;
    }

    /**
     * The attributes of the accelerator. Fields documented below.
     */
    public readonly attributes!: pulumi.Output<outputs.globalaccelerator.AcceleratorAttributes | undefined>;
    /**
     * The DNS name of the accelerator. For example, `a5d53ff5ee6bca4ce.awsglobalaccelerator.com`.
     * * `hostedZoneId` --  The Global Accelerator Route 53 zone ID that can be used to
     * route an [Alias Resource Record Set][1] to the Global Accelerator. This attribute
     * is simply an alias for the zone ID `Z2BJ6XQ5FK7U4H`.
     */
    public /*out*/ readonly dnsName!: pulumi.Output<string>;
    /**
     * Indicates whether the accelerator is enabled. The value is true or false. The default value is true.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly hostedZoneId!: pulumi.Output<string>;
    /**
     * The value for the address type must be `IPV4`.
     */
    public readonly ipAddressType!: pulumi.Output<string | undefined>;
    /**
     * IP address set associated with the accelerator.
     */
    public /*out*/ readonly ipSets!: pulumi.Output<outputs.globalaccelerator.AcceleratorIpSet[]>;
    /**
     * The name of the accelerator.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a Accelerator resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: AcceleratorArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AcceleratorArgs | AcceleratorState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as AcceleratorState | undefined;
            inputs["attributes"] = state ? state.attributes : undefined;
            inputs["dnsName"] = state ? state.dnsName : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["hostedZoneId"] = state ? state.hostedZoneId : undefined;
            inputs["ipAddressType"] = state ? state.ipAddressType : undefined;
            inputs["ipSets"] = state ? state.ipSets : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as AcceleratorArgs | undefined;
            inputs["attributes"] = args ? args.attributes : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["ipAddressType"] = args ? args.ipAddressType : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["dnsName"] = undefined /*out*/;
            inputs["hostedZoneId"] = undefined /*out*/;
            inputs["ipSets"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Accelerator.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Accelerator resources.
 */
export interface AcceleratorState {
    /**
     * The attributes of the accelerator. Fields documented below.
     */
    readonly attributes?: pulumi.Input<inputs.globalaccelerator.AcceleratorAttributes>;
    /**
     * The DNS name of the accelerator. For example, `a5d53ff5ee6bca4ce.awsglobalaccelerator.com`.
     * * `hostedZoneId` --  The Global Accelerator Route 53 zone ID that can be used to
     * route an [Alias Resource Record Set][1] to the Global Accelerator. This attribute
     * is simply an alias for the zone ID `Z2BJ6XQ5FK7U4H`.
     */
    readonly dnsName?: pulumi.Input<string>;
    /**
     * Indicates whether the accelerator is enabled. The value is true or false. The default value is true.
     */
    readonly enabled?: pulumi.Input<boolean>;
    readonly hostedZoneId?: pulumi.Input<string>;
    /**
     * The value for the address type must be `IPV4`.
     */
    readonly ipAddressType?: pulumi.Input<string>;
    /**
     * IP address set associated with the accelerator.
     */
    readonly ipSets?: pulumi.Input<pulumi.Input<inputs.globalaccelerator.AcceleratorIpSet>[]>;
    /**
     * The name of the accelerator.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a Accelerator resource.
 */
export interface AcceleratorArgs {
    /**
     * The attributes of the accelerator. Fields documented below.
     */
    readonly attributes?: pulumi.Input<inputs.globalaccelerator.AcceleratorAttributes>;
    /**
     * Indicates whether the accelerator is enabled. The value is true or false. The default value is true.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The value for the address type must be `IPV4`.
     */
    readonly ipAddressType?: pulumi.Input<string>;
    /**
     * The name of the accelerator.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
