// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

import {ParameterType} from "./parameterType";

/**
 * Provides an SSM Parameter resource.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const foo = new aws.ssm.Parameter("foo", {
 *     type: "String",
 *     value: "bar",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_parameter.html.markdown.
 */
export class Parameter extends pulumi.CustomResource {
    /**
     * Get an existing Parameter resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ParameterState, opts?: pulumi.CustomResourceOptions): Parameter {
        return new Parameter(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:ssm/parameter:Parameter';

    /**
     * Returns true if the given object is an instance of Parameter.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Parameter {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Parameter.__pulumiType;
    }

    /**
     * A regular expression used to validate the parameter value.
     */
    public readonly allowedPattern!: pulumi.Output<string | undefined>;
    /**
     * The ARN of the parameter.
     */
    public readonly arn!: pulumi.Output<string>;
    /**
     * The description of the parameter.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The KMS key id or arn for encrypting a SecureString.
     */
    public readonly keyId!: pulumi.Output<string>;
    /**
     * The name of the parameter. If the name contains a path (e.g. any forward slashes (`/`)), it must be fully qualified with a leading forward slash (`/`). For additional requirements and constraints, see the [AWS SSM User Guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-parameter-name-constraints.html).
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Overwrite an existing parameter. If not specified, will default to `false` if the resource has not been created by this provider to avoid overwrite of existing resource and will default to `true` otherwise (lifecycle rules should then be used to manage the update behavior).
     */
    public readonly overwrite!: pulumi.Output<boolean | undefined>;
    /**
     * A mapping of tags to assign to the object.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The tier of the parameter. If not specified, will default to `Standard`. Valid tiers are `Standard` and `Advanced`. For more information on parameter tiers, see the [AWS SSM Parameter tier comparison and guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html).
     */
    public readonly tier!: pulumi.Output<string | undefined>;
    /**
     * The type of the parameter. Valid types are `String`, `StringList` and `SecureString`.
     */
    public readonly type!: pulumi.Output<ParameterType>;
    /**
     * The value of the parameter.
     */
    public readonly value!: pulumi.Output<string>;
    /**
     * The version of the parameter.
     */
    public /*out*/ readonly version!: pulumi.Output<number>;

    /**
     * Create a Parameter resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ParameterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ParameterArgs | ParameterState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ParameterState | undefined;
            inputs["allowedPattern"] = state ? state.allowedPattern : undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["keyId"] = state ? state.keyId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["overwrite"] = state ? state.overwrite : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["tier"] = state ? state.tier : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["value"] = state ? state.value : undefined;
            inputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as ParameterArgs | undefined;
            if (!args || args.type === undefined) {
                throw new Error("Missing required property 'type'");
            }
            if (!args || args.value === undefined) {
                throw new Error("Missing required property 'value'");
            }
            inputs["allowedPattern"] = args ? args.allowedPattern : undefined;
            inputs["arn"] = args ? args.arn : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["keyId"] = args ? args.keyId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["overwrite"] = args ? args.overwrite : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["tier"] = args ? args.tier : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["value"] = args ? args.value : undefined;
            inputs["version"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Parameter.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Parameter resources.
 */
export interface ParameterState {
    /**
     * A regular expression used to validate the parameter value.
     */
    readonly allowedPattern?: pulumi.Input<string>;
    /**
     * The ARN of the parameter.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The description of the parameter.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The KMS key id or arn for encrypting a SecureString.
     */
    readonly keyId?: pulumi.Input<string>;
    /**
     * The name of the parameter. If the name contains a path (e.g. any forward slashes (`/`)), it must be fully qualified with a leading forward slash (`/`). For additional requirements and constraints, see the [AWS SSM User Guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-parameter-name-constraints.html).
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Overwrite an existing parameter. If not specified, will default to `false` if the resource has not been created by this provider to avoid overwrite of existing resource and will default to `true` otherwise (lifecycle rules should then be used to manage the update behavior).
     */
    readonly overwrite?: pulumi.Input<boolean>;
    /**
     * A mapping of tags to assign to the object.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The tier of the parameter. If not specified, will default to `Standard`. Valid tiers are `Standard` and `Advanced`. For more information on parameter tiers, see the [AWS SSM Parameter tier comparison and guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html).
     */
    readonly tier?: pulumi.Input<string>;
    /**
     * The type of the parameter. Valid types are `String`, `StringList` and `SecureString`.
     */
    readonly type?: pulumi.Input<ParameterType>;
    /**
     * The value of the parameter.
     */
    readonly value?: pulumi.Input<string>;
    /**
     * The version of the parameter.
     */
    readonly version?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Parameter resource.
 */
export interface ParameterArgs {
    /**
     * A regular expression used to validate the parameter value.
     */
    readonly allowedPattern?: pulumi.Input<string>;
    /**
     * The ARN of the parameter.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The description of the parameter.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The KMS key id or arn for encrypting a SecureString.
     */
    readonly keyId?: pulumi.Input<string>;
    /**
     * The name of the parameter. If the name contains a path (e.g. any forward slashes (`/`)), it must be fully qualified with a leading forward slash (`/`). For additional requirements and constraints, see the [AWS SSM User Guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-parameter-name-constraints.html).
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Overwrite an existing parameter. If not specified, will default to `false` if the resource has not been created by this provider to avoid overwrite of existing resource and will default to `true` otherwise (lifecycle rules should then be used to manage the update behavior).
     */
    readonly overwrite?: pulumi.Input<boolean>;
    /**
     * A mapping of tags to assign to the object.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * The tier of the parameter. If not specified, will default to `Standard`. Valid tiers are `Standard` and `Advanced`. For more information on parameter tiers, see the [AWS SSM Parameter tier comparison and guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html).
     */
    readonly tier?: pulumi.Input<string>;
    /**
     * The type of the parameter. Valid types are `String`, `StringList` and `SecureString`.
     */
    readonly type: pulumi.Input<ParameterType>;
    /**
     * The value of the parameter.
     */
    readonly value: pulumi.Input<string>;
}
