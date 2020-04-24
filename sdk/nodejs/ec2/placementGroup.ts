// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

import {PlacementStrategy} from "./placementStrategy";

/**
 * Provides an EC2 placement group. Read more about placement groups
 * in [AWS Docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const web = new aws.ec2.PlacementGroup("web", {
 *     strategy: "cluster",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/placement_group.html.markdown.
 */
export class PlacementGroup extends pulumi.CustomResource {
    /**
     * Get an existing PlacementGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PlacementGroupState, opts?: pulumi.CustomResourceOptions): PlacementGroup {
        return new PlacementGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:ec2/placementGroup:PlacementGroup';

    /**
     * Returns true if the given object is an instance of PlacementGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PlacementGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PlacementGroup.__pulumiType;
    }

    /**
     * The name of the placement group.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the placement group.
     */
    public /*out*/ readonly placementGroupId!: pulumi.Output<string>;
    /**
     * The placement strategy.
     */
    public readonly strategy!: pulumi.Output<PlacementStrategy>;
    /**
     * Key-value map of resource tags.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a PlacementGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PlacementGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PlacementGroupArgs | PlacementGroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as PlacementGroupState | undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["placementGroupId"] = state ? state.placementGroupId : undefined;
            inputs["strategy"] = state ? state.strategy : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as PlacementGroupArgs | undefined;
            if (!args || args.strategy === undefined) {
                throw new Error("Missing required property 'strategy'");
            }
            inputs["name"] = args ? args.name : undefined;
            inputs["strategy"] = args ? args.strategy : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["placementGroupId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(PlacementGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PlacementGroup resources.
 */
export interface PlacementGroupState {
    /**
     * The name of the placement group.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the placement group.
     */
    readonly placementGroupId?: pulumi.Input<string>;
    /**
     * The placement strategy.
     */
    readonly strategy?: pulumi.Input<PlacementStrategy>;
    /**
     * Key-value map of resource tags.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a PlacementGroup resource.
 */
export interface PlacementGroupArgs {
    /**
     * The name of the placement group.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The placement strategy.
     */
    readonly strategy: pulumi.Input<PlacementStrategy>;
    /**
     * Key-value map of resource tags.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
