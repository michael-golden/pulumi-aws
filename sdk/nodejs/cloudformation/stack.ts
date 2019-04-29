// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a CloudFormation Stack resource.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const network = new aws.cloudformation.Stack("network", {
 *     parameters: {
 *         VPCCidr: "10.0.0.0/16",
 *     },
 *     templateBody: `{
 *   "Parameters" : {
 *     "VPCCidr" : {
 *       "Type" : "String",
 *       "Default" : "10.0.0.0/16",
 *       "Description" : "Enter the CIDR block for the VPC. Default is 10.0.0.0/16."
 *     }
 *   },
 *   "Resources" : {
 *     "myVpc": {
 *       "Type" : "AWS::EC2::VPC",
 *       "Properties" : {
 *         "CidrBlock" : { "Ref" : "VPCCidr" },
 *         "Tags" : [
 *           {"Key": "Name", "Value": "Primary_CF_VPC"}
 *         ]
 *       }
 *     }
 *   }
 * }
 * `,
 * });
 * ```
 */
export class Stack extends pulumi.CustomResource {
    /**
     * Get an existing Stack resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StackState, opts?: pulumi.CustomResourceOptions): Stack {
        return new Stack(name, <any>state, { ...opts, id: id });
    }

    /**
     * A list of capabilities.
     * Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, or `CAPABILITY_AUTO_EXPAND`
     */
    public readonly capabilities: pulumi.Output<string[] | undefined>;
    /**
     * Set to true to disable rollback of the stack if stack creation failed.
     * Conflicts with `on_failure`.
     */
    public readonly disableRollback: pulumi.Output<boolean | undefined>;
    /**
     * The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
     */
    public readonly iamRoleArn: pulumi.Output<string | undefined>;
    /**
     * Stack name.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * A list of SNS topic ARNs to publish stack related events.
     */
    public readonly notificationArns: pulumi.Output<string[] | undefined>;
    /**
     * Action to be taken if stack creation fails. This must be
     * one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.
     */
    public readonly onFailure: pulumi.Output<string | undefined>;
    /**
     * A map of outputs from the stack.
     */
    public /*out*/ readonly outputs: pulumi.Output<{[key: string]: any}>;
    /**
     * A map of Parameter structures that specify input parameters for the stack.
     */
    public readonly parameters: pulumi.Output<{[key: string]: any}>;
    /**
     * Structure containing the stack policy body.
     * Conflicts w/ `policy_url`.
     */
    public readonly policyBody: pulumi.Output<string>;
    /**
     * Location of a file containing the stack policy.
     * Conflicts w/ `policy_body`.
     */
    public readonly policyUrl: pulumi.Output<string | undefined>;
    /**
     * A list of tags to associate with this stack.
     */
    public readonly tags: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * Structure containing the template body (max size: 51,200 bytes).
     */
    public readonly templateBody: pulumi.Output<string>;
    /**
     * Location of a file containing the template body (max size: 460,800 bytes).
     */
    public readonly templateUrl: pulumi.Output<string | undefined>;
    /**
     * The amount of time that can pass before the stack status becomes `CREATE_FAILED`.
     */
    public readonly timeoutInMinutes: pulumi.Output<number | undefined>;

    /**
     * Create a Stack resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: StackArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: StackArgs | StackState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: StackState = argsOrState as StackState | undefined;
            inputs["capabilities"] = state ? state.capabilities : undefined;
            inputs["disableRollback"] = state ? state.disableRollback : undefined;
            inputs["iamRoleArn"] = state ? state.iamRoleArn : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["notificationArns"] = state ? state.notificationArns : undefined;
            inputs["onFailure"] = state ? state.onFailure : undefined;
            inputs["outputs"] = state ? state.outputs : undefined;
            inputs["parameters"] = state ? state.parameters : undefined;
            inputs["policyBody"] = state ? state.policyBody : undefined;
            inputs["policyUrl"] = state ? state.policyUrl : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["templateBody"] = state ? state.templateBody : undefined;
            inputs["templateUrl"] = state ? state.templateUrl : undefined;
            inputs["timeoutInMinutes"] = state ? state.timeoutInMinutes : undefined;
        } else {
            const args = argsOrState as StackArgs | undefined;
            inputs["capabilities"] = args ? args.capabilities : undefined;
            inputs["disableRollback"] = args ? args.disableRollback : undefined;
            inputs["iamRoleArn"] = args ? args.iamRoleArn : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["notificationArns"] = args ? args.notificationArns : undefined;
            inputs["onFailure"] = args ? args.onFailure : undefined;
            inputs["parameters"] = args ? args.parameters : undefined;
            inputs["policyBody"] = args ? args.policyBody : undefined;
            inputs["policyUrl"] = args ? args.policyUrl : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["templateBody"] = args ? args.templateBody : undefined;
            inputs["templateUrl"] = args ? args.templateUrl : undefined;
            inputs["timeoutInMinutes"] = args ? args.timeoutInMinutes : undefined;
            inputs["outputs"] = undefined /*out*/;
        }
        super("aws:cloudformation/stack:Stack", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Stack resources.
 */
export interface StackState {
    /**
     * A list of capabilities.
     * Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, or `CAPABILITY_AUTO_EXPAND`
     */
    readonly capabilities?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Set to true to disable rollback of the stack if stack creation failed.
     * Conflicts with `on_failure`.
     */
    readonly disableRollback?: pulumi.Input<boolean>;
    /**
     * The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
     */
    readonly iamRoleArn?: pulumi.Input<string>;
    /**
     * Stack name.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A list of SNS topic ARNs to publish stack related events.
     */
    readonly notificationArns?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Action to be taken if stack creation fails. This must be
     * one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.
     */
    readonly onFailure?: pulumi.Input<string>;
    /**
     * A map of outputs from the stack.
     */
    readonly outputs?: pulumi.Input<{[key: string]: any}>;
    /**
     * A map of Parameter structures that specify input parameters for the stack.
     */
    readonly parameters?: pulumi.Input<{[key: string]: any}>;
    /**
     * Structure containing the stack policy body.
     * Conflicts w/ `policy_url`.
     */
    readonly policyBody?: pulumi.Input<string>;
    /**
     * Location of a file containing the stack policy.
     * Conflicts w/ `policy_body`.
     */
    readonly policyUrl?: pulumi.Input<string>;
    /**
     * A list of tags to associate with this stack.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * Structure containing the template body (max size: 51,200 bytes).
     */
    readonly templateBody?: pulumi.Input<string>;
    /**
     * Location of a file containing the template body (max size: 460,800 bytes).
     */
    readonly templateUrl?: pulumi.Input<string>;
    /**
     * The amount of time that can pass before the stack status becomes `CREATE_FAILED`.
     */
    readonly timeoutInMinutes?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Stack resource.
 */
export interface StackArgs {
    /**
     * A list of capabilities.
     * Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, or `CAPABILITY_AUTO_EXPAND`
     */
    readonly capabilities?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Set to true to disable rollback of the stack if stack creation failed.
     * Conflicts with `on_failure`.
     */
    readonly disableRollback?: pulumi.Input<boolean>;
    /**
     * The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
     */
    readonly iamRoleArn?: pulumi.Input<string>;
    /**
     * Stack name.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A list of SNS topic ARNs to publish stack related events.
     */
    readonly notificationArns?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Action to be taken if stack creation fails. This must be
     * one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.
     */
    readonly onFailure?: pulumi.Input<string>;
    /**
     * A map of Parameter structures that specify input parameters for the stack.
     */
    readonly parameters?: pulumi.Input<{[key: string]: any}>;
    /**
     * Structure containing the stack policy body.
     * Conflicts w/ `policy_url`.
     */
    readonly policyBody?: pulumi.Input<string>;
    /**
     * Location of a file containing the stack policy.
     * Conflicts w/ `policy_body`.
     */
    readonly policyUrl?: pulumi.Input<string>;
    /**
     * A list of tags to associate with this stack.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * Structure containing the template body (max size: 51,200 bytes).
     */
    readonly templateBody?: pulumi.Input<string>;
    /**
     * Location of a file containing the template body (max size: 460,800 bytes).
     */
    readonly templateUrl?: pulumi.Input<string>;
    /**
     * The amount of time that can pass before the stack status becomes `CREATE_FAILED`.
     */
    readonly timeoutInMinutes?: pulumi.Input<number>;
}
