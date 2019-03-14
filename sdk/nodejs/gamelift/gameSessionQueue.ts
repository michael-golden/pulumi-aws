// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Provides an Gamelift Game Session Queue resource.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const test = new aws.gamelift.GameSessionQueue("test", {
 *     destinations: [
 *         aws_gamelift_fleet_us_west_2_fleet.arn,
 *         aws_gamelift_fleet_eu_central_1_fleet.arn,
 *     ],
 *     playerLatencyPolicies: [
 *         {
 *             maximumIndividualPlayerLatencyMilliseconds: 100,
 *             policyDurationSeconds: 5,
 *         },
 *         {
 *             maximumIndividualPlayerLatencyMilliseconds: 200,
 *         },
 *     ],
 *     timeoutInSeconds: 60,
 * });
 * ```
 */
export class GameSessionQueue extends pulumi.CustomResource {
    /**
     * Get an existing GameSessionQueue resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GameSessionQueueState, opts?: pulumi.CustomResourceOptions): GameSessionQueue {
        return new GameSessionQueue(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<GameSessionQueueResult> {
        return ctx.list({...args, type: 'aws:gamelift/gameSessionQueue:GameSessionQueue'});
    }

    public static addAdmissionPolicy(policy: pulumi.policy.AdmissionPolicy): void {
        pulumi.runtime.addAdmissionPolicy({
            ...policy,
            pulumiType: 'aws:gamelift/gameSessionQueue:GameSessionQueue',
        });
    }
    /**
     * Game Session Queue ARN.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * List of fleet/alias ARNs used by session queue for placing game sessions.
     */
    public readonly destinations: pulumi.Output<string[] | undefined>;
    /**
     * Name of the session queue.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * One or more policies used to choose fleet based on player latency. See below.
     */
    public readonly playerLatencyPolicies: pulumi.Output<{ maximumIndividualPlayerLatencyMilliseconds: number, policyDurationSeconds?: number }[] | undefined>;
    /**
     * Maximum time a game session request can remain in the queue.
     */
    public readonly timeoutInSeconds: pulumi.Output<number | undefined>;

    /**
     * Create a GameSessionQueue resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: GameSessionQueueArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GameSessionQueueArgs | GameSessionQueueState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: GameSessionQueueState = argsOrState as GameSessionQueueState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["destinations"] = state ? state.destinations : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["playerLatencyPolicies"] = state ? state.playerLatencyPolicies : undefined;
            inputs["timeoutInSeconds"] = state ? state.timeoutInSeconds : undefined;
        } else {
            const args = argsOrState as GameSessionQueueArgs | undefined;
            inputs["destinations"] = args ? args.destinations : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["playerLatencyPolicies"] = args ? args.playerLatencyPolicies : undefined;
            inputs["timeoutInSeconds"] = args ? args.timeoutInSeconds : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super("aws:gamelift/gameSessionQueue:GameSessionQueue", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GameSessionQueue resources.
 */
export interface GameSessionQueueState {
    /**
     * Game Session Queue ARN.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * List of fleet/alias ARNs used by session queue for placing game sessions.
     */
    readonly destinations?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Name of the session queue.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * One or more policies used to choose fleet based on player latency. See below.
     */
    readonly playerLatencyPolicies?: pulumi.Input<pulumi.Input<{ maximumIndividualPlayerLatencyMilliseconds: pulumi.Input<number>, policyDurationSeconds?: pulumi.Input<number> }>[]>;
    /**
     * Maximum time a game session request can remain in the queue.
     */
    readonly timeoutInSeconds?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a GameSessionQueue resource.
 */
export interface GameSessionQueueArgs {
    /**
     * List of fleet/alias ARNs used by session queue for placing game sessions.
     */
    readonly destinations?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Name of the session queue.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * One or more policies used to choose fleet based on player latency. See below.
     */
    readonly playerLatencyPolicies?: pulumi.Input<pulumi.Input<{ maximumIndividualPlayerLatencyMilliseconds: pulumi.Input<number>, policyDurationSeconds?: pulumi.Input<number> }>[]>;
    /**
     * Maximum time a game session request can remain in the queue.
     */
    readonly timeoutInSeconds?: pulumi.Input<number>;
}

/**
 * The live GameSessionQueue resource.
 */
export interface GameSessionQueueResult {
    /**
     * Game Session Queue ARN.
     */
    readonly arn: string;
    /**
     * List of fleet/alias ARNs used by session queue for placing game sessions.
     */
    readonly destinations?: string[];
    /**
     * Name of the session queue.
     */
    readonly name: string;
    /**
     * One or more policies used to choose fleet based on player latency. See below.
     */
    readonly playerLatencyPolicies?: { maximumIndividualPlayerLatencyMilliseconds: number, policyDurationSeconds?: number }[];
    /**
     * Maximum time a game session request can remain in the queue.
     */
    readonly timeoutInSeconds?: number;
}
