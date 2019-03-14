// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Manages an AWS DataSync Agent deployed on premises.
 * 
 * > **NOTE:** One of `activation_key` or `ip_address` must be provided for resource creation (agent activation). Neither is required for resource import. If using `ip_address`, Terraform must be able to make an HTTP (port 80) GET request to the specified IP address from where it is running. The agent will turn off that HTTP server after activation.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.datasync.Agent("example", {
 *     ipAddress: "1.2.3.4",
 * });
 * ```
 */
export class Agent extends pulumi.CustomResource {
    /**
     * Get an existing Agent resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AgentState, opts?: pulumi.CustomResourceOptions): Agent {
        return new Agent(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<AgentResult> {
        return ctx.list({...args, type: 'aws:datasync/agent:Agent'});
    }

    public static addAdmissionPolicy(policy: pulumi.policy.AdmissionPolicy): void {
        pulumi.runtime.addAdmissionPolicy({
            ...policy,
            pulumiType: 'aws:datasync/agent:Agent',
        });
    }
    /**
     * DataSync Agent activation key during resource creation. Conflicts with `ip_address`. If an `ip_address` is provided instead, Terraform will retrieve the `activation_key` as part of the resource creation.
     */
    public readonly activationKey: pulumi.Output<string>;
    /**
     * Amazon Resource Name (ARN) of the DataSync Agent.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. DataSync Agent must be accessible on port 80 from where Terraform is running.
     */
    public readonly ipAddress: pulumi.Output<string>;
    /**
     * Name of the DataSync Agent.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * Key-value pairs of resource tags to assign to the DataSync Agent.
     */
    public readonly tags: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a Agent resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: AgentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AgentArgs | AgentState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: AgentState = argsOrState as AgentState | undefined;
            inputs["activationKey"] = state ? state.activationKey : undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["ipAddress"] = state ? state.ipAddress : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as AgentArgs | undefined;
            inputs["activationKey"] = args ? args.activationKey : undefined;
            inputs["ipAddress"] = args ? args.ipAddress : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super("aws:datasync/agent:Agent", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Agent resources.
 */
export interface AgentState {
    /**
     * DataSync Agent activation key during resource creation. Conflicts with `ip_address`. If an `ip_address` is provided instead, Terraform will retrieve the `activation_key` as part of the resource creation.
     */
    readonly activationKey?: pulumi.Input<string>;
    /**
     * Amazon Resource Name (ARN) of the DataSync Agent.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. DataSync Agent must be accessible on port 80 from where Terraform is running.
     */
    readonly ipAddress?: pulumi.Input<string>;
    /**
     * Name of the DataSync Agent.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Key-value pairs of resource tags to assign to the DataSync Agent.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a Agent resource.
 */
export interface AgentArgs {
    /**
     * DataSync Agent activation key during resource creation. Conflicts with `ip_address`. If an `ip_address` is provided instead, Terraform will retrieve the `activation_key` as part of the resource creation.
     */
    readonly activationKey?: pulumi.Input<string>;
    /**
     * DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. DataSync Agent must be accessible on port 80 from where Terraform is running.
     */
    readonly ipAddress?: pulumi.Input<string>;
    /**
     * Name of the DataSync Agent.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Key-value pairs of resource tags to assign to the DataSync Agent.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The live Agent resource.
 */
export interface AgentResult {
    /**
     * DataSync Agent activation key during resource creation. Conflicts with `ip_address`. If an `ip_address` is provided instead, Terraform will retrieve the `activation_key` as part of the resource creation.
     */
    readonly activationKey: string;
    /**
     * Amazon Resource Name (ARN) of the DataSync Agent.
     */
    readonly arn: string;
    /**
     * DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. DataSync Agent must be accessible on port 80 from where Terraform is running.
     */
    readonly ipAddress: string;
    /**
     * Name of the DataSync Agent.
     */
    readonly name: string;
    /**
     * Key-value pairs of resource tags to assign to the DataSync Agent.
     */
    readonly tags?: {[key: string]: string};
}
