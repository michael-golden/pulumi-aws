// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides an ElastiCache parameter group resource.
 * 
 * > **NOTE:** Attempting to remove the `reserved-memory` parameter when `family` is set to `redis2.6` or `redis2.8` may show a perpetual difference in this provider due to an Elasticache API limitation. Leave that parameter configured with any value to workaround the issue.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const defaultParameterGroup = new aws.elasticache.ParameterGroup("default", {
 *     family: "redis2.8",
 *     parameters: [
 *         {
 *             name: "activerehashing",
 *             value: "yes",
 *         },
 *         {
 *             name: "min-slaves-to-write",
 *             value: "2",
 *         },
 *     ],
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elasticache_parameter_group.html.markdown.
 */
export class ParameterGroup extends pulumi.CustomResource {
    /**
     * Get an existing ParameterGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ParameterGroupState, opts?: pulumi.CustomResourceOptions): ParameterGroup {
        return new ParameterGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:elasticache/parameterGroup:ParameterGroup';

    /**
     * Returns true if the given object is an instance of ParameterGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ParameterGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ParameterGroup.__pulumiType;
    }

    /**
     * The description of the ElastiCache parameter group. Defaults to "Managed by Pulumi".
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The family of the ElastiCache parameter group.
     */
    public readonly family!: pulumi.Output<string>;
    /**
     * The name of the ElastiCache parameter.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A list of ElastiCache parameters to apply.
     */
    public readonly parameters!: pulumi.Output<outputs.elasticache.ParameterGroupParameter[] | undefined>;

    /**
     * Create a ParameterGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ParameterGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ParameterGroupArgs | ParameterGroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ParameterGroupState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["family"] = state ? state.family : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["parameters"] = state ? state.parameters : undefined;
        } else {
            const args = argsOrState as ParameterGroupArgs | undefined;
            if (!args || args.family === undefined) {
                throw new Error("Missing required property 'family'");
            }
            inputs["description"] = (args ? args.description : undefined) || "Managed by Pulumi";
            inputs["family"] = args ? args.family : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["parameters"] = args ? args.parameters : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ParameterGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ParameterGroup resources.
 */
export interface ParameterGroupState {
    /**
     * The description of the ElastiCache parameter group. Defaults to "Managed by Pulumi".
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The family of the ElastiCache parameter group.
     */
    readonly family?: pulumi.Input<string>;
    /**
     * The name of the ElastiCache parameter.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A list of ElastiCache parameters to apply.
     */
    readonly parameters?: pulumi.Input<pulumi.Input<inputs.elasticache.ParameterGroupParameter>[]>;
}

/**
 * The set of arguments for constructing a ParameterGroup resource.
 */
export interface ParameterGroupArgs {
    /**
     * The description of the ElastiCache parameter group. Defaults to "Managed by Pulumi".
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The family of the ElastiCache parameter group.
     */
    readonly family: pulumi.Input<string>;
    /**
     * The name of the ElastiCache parameter.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A list of ElastiCache parameters to apply.
     */
    readonly parameters?: pulumi.Input<pulumi.Input<inputs.elasticache.ParameterGroupParameter>[]>;
}
